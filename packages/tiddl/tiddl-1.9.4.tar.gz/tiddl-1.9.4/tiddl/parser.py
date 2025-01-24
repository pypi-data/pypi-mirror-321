import os
import argparse

from .types import TRACK_QUALITY
from .types.track import TrackQuality


def shouldNotColor() -> bool:
    # TODO: add more checks ✨
    checks = ["NO_COLOR" in os.environ]
    return any(checks)


parser = argparse.ArgumentParser(
    description="\033[4mTIDDL\033[0m - Tidal Downloader",
    epilog="options defaults will be fetched from your config file.",
)

parser.add_argument(
    "input",
    type=str,
    nargs="*",
    help="track, album, playlist or artist - must be url, single id will be treated as track",
)

parser.add_argument(
    "-o",
    type=str,
    nargs="?",
    const=True,
    help="output file template, more info https://github.com/oskvr37/tiddl?tab=readme-ov-file#file-formatting",
    dest="file_template",
)

parser.add_argument(
    "-p",
    type=str,
    nargs="?",
    const=True,
    help="download destination path",
    dest="download_path",
)

parser.add_argument(
    "-e",
    type=str,
    nargs="?",
    const=True,
    help="choose file extension",
    dest="file_extension",
)

QUALITY_ARGS: dict[str, TrackQuality] = {
    details["arg"]: quality for quality, details in TRACK_QUALITY.items()
}

parser.add_argument(
    "-q",
    nargs="?",
    help="track quality",
    dest="quality",
    choices=QUALITY_ARGS.keys(),
)

parser.add_argument(
    "-is",
    help="include artist EPs and singles when downloading artist",
    dest="include_singles",
    action="store_true",
)

parser.add_argument(
    "-s",
    help="save options to config // show config file",
    dest="save_options",
    action="store_true",
)

parser.add_argument(
    "-i",
    type=str,
    nargs="?",
    const=True,
    help="choose a file with urls (.txt file separated with newlines or .json list)",
    dest="input_file",
    default="",
)

parser.add_argument(
    "--no-skip",
    help="dont skip already downloaded tracks",
    action="store_true",
)

parser.add_argument(
    "--silent",
    help="silent mode",
    action="store_true",
)

parser.add_argument(
    "--verbose",
    help="show debug logs",
    action="store_true",
)

parser.add_argument(
    "--no-color",
    help="suppress output colors",
    action="store_true",
    default=shouldNotColor(),
)
