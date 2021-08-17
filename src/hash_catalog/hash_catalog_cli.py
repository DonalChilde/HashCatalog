import argparse
import sys
import os
from hash_catalog import VERSION
from pathlib import Path
from hash_catalog.utility_lib.argparse_utilities import ArgumentParser, ReadableDir


def parse_args():
    parser = ArgumentParser(
        prog="HashCatalog", description="A program to generate and verify file hashes."
    )
    parser.version = VERSION
    parser.add_argument("input_path", action=ReadableDir)
    parser.add_argument("glob")
    #
    # ... configure command line arguments ...
    #
    return parser.parse_args()


def do_stuff(args):
    print(args.input_path)
    list_of_paths = list(args.input_path.glob(args.glob))
    print(list_of_paths[:10])
    print(len(list_of_paths))
    #
    # ... main functionality goes in here ...
    #


def main(argv=None) -> int:
    if argv is None:
        argv = sys.argv
    args = parse_args()
    do_stuff(args)
    return 0


if __name__ == "__main__":
    # support exit code returns
    sys.exit(main())
