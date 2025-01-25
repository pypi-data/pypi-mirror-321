"""Main entry point for 4chan_ripper"""

import logging

from argparse import ArgumentParser
from pathlib import Path
from random import choice
from time import sleep
from urllib.parse import urlparse

import requests

from bs4 import BeautifulSoup
from prompt_toolkit.shortcuts import checkboxlist_dialog
from rich.logging import RichHandler
from rich.progress import track
from spawn_user_agent.user_agent import SpawnUserAgent

log = logging.getLogger(__name__)

_MAX_RETRIES = 3
_UAS = SpawnUserAgent.generate_all()


class RippableThread:
    """Represents a thread on 4chan to rip"""

    def __init__(self, board: str, thread: str, is_photoset: bool = False) -> None:
        """Initializer, creates a new RippableThread object

        Args:
            board (str): The short code name of the board to target (e.g. "b")
            thread (str): The id of the thread to rip (e.g. "12345")
            is_photoset (bool): Indicates if the ripped thread should be treated as a photoset (i.e. don't include date in folder name, also extract description). Defaults to False.
        """
        self.board = board
        self.thread = thread
        self.is_photoset = is_photoset

        self._headers = {"User-Agent": choice(_UAS)}
        posts = requests.get(f'https://a.4cdn.org/{board}/thread/{thread}.json', headers=self._headers).json()["posts"]
        self.file_list = {f"{p['tim']}{p['ext']}" for p in posts if "tim" in p and "ext" in p}

        op = posts[0]
        self._subject = op.get("sub") or op.get("semantic_url", thread)
        self._comment = op.get("com")

    def download(self, out_dir: Path) -> bool:
        """Actually download try downloading the thread represented by this RippableThread.

        Args:
            out_dir (Path): The output directory to save downloaded files to.

        Returns:
            bool: `True` if there were no errors
        """
        (output_dir := out_dir / ((f"{self.thread} - " if not self.is_photoset else "") + self._subject.replace("/", "_").replace(":", "").replace("&amp;", "&"))).mkdir(parents=True, exist_ok=True)
        log.info("Using folder: '%s'", output_dir)

        if self.is_photoset and self._comment and len((txt := BeautifulSoup(self._comment, "lxml").get_text("\n"))) > 50:
            log.info("Writing info.txt entry to '%s'...", output_dir)
            (output_dir / "info.txt").write_text(txt)

        success = True
        for fn in track(self.file_list, f"Processing '{self._subject}'..."):
            if (out_file := output_dir / fn).is_file():
                continue

            attempt = 1
            while attempt <= _MAX_RETRIES:
                try:
                    if (r := requests.get(f"https://i.4cdn.org/{self.board}/{fn}", headers=self._headers)).status_code == requests.codes.too_many_requests:
                        log.warning("Throttled by server when downloading '%s', sleeping 5s.  This was attempt %d of %d", fn, attempt, _MAX_RETRIES)
                        sleep(5)
                    else:
                        body = r.content
                        if any(s for s in body):  # deleted/404'd media is sometimes all null bytes, these should be skipped.
                            out_file.write_bytes(body)
                        break
                except Exception:
                    log.warning("Failed to download '%s', this was attempt %d of %d", fn, attempt, _MAX_RETRIES, exc_info=True)

                attempt += 1

            success &= attempt <= _MAX_RETRIES

        return success


def _main() -> None:
    """Main driver, invoked when this file is run directly."""
    cli_parser = ArgumentParser(description="4chan ripper CLI")
    cli_parser.add_argument('-b', type=str, metavar="board_id", default="hr", help="The short id of the board to target. Ignored if the program was not started in interactive mode.  Default is hr")
    cli_parser.add_argument('-i', action='store_true', help="Causes the archive file to get ignored. Only applicable in interactive mode.")
    cli_parser.add_argument('-s', action='store_true', help="Treat the input urls as a photoset to rip")
    cli_parser.add_argument('-o', type=Path, default=Path("."), metavar="output_directory", help="The output directory. Defaults to the current working directory.")
    cli_parser.add_argument('urls', type=str, nargs='*', help='the urls to process')
    args = cli_parser.parse_args()

    log.addHandler(RichHandler(rich_tracebacks=True))
    log.setLevel(logging.INFO)

    if args.urls:
        for url in args.urls:
            board, _, no = urlparse(url).path.split("/")[1:4]
            RippableThread(board, no, args.s).download(args.o)
        return

    archived = set(archive_file.read_text().splitlines()) if not args.i and (archive_file := args.o / ".archive.txt").is_file() else set()

    targets = {}
    display_pairs = {}
    for l in [tr.select("td") for tr in BeautifulSoup(requests.get(f"https://boards.4chan.org/{args.b}/archive").text, 'lxml').select(".flashListing tbody tr")]:
        if (args.b + (id := l[0].string)) not in archived:
            targets[id] = (rt := RippableThread(args.b, id))
            display_pairs[id] = f"[{len(rt.file_list)}] {l[1].get_text()}"

    if not display_pairs:
        log.warning("No threads matching the specified criteria are available to rip or they have all already been ripped.  Doing nothing.")
        return

    if not (selected := checkboxlist_dialog("Select threads to rip", values=list(display_pairs.items())).run()):
        return

    display_pairs = {id: text for id, text in display_pairs.items() if id in selected}
    if (photoset_selected := checkboxlist_dialog("Are any of these photosets?", values=list(display_pairs.items())).run()) is None:
        return

    for id in photoset_selected:
        targets[id].is_photoset = True

    if (successful_downloads := [f"{targets[id].board}{id}" for id in selected if targets[id].download(args.o)]) and not args.i:
        with archive_file.open("a") as f:
            f.write("\n".join(successful_downloads) + "\n")


if __name__ == "__main__":
    _main()
