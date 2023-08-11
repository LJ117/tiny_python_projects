#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Gematria
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Gematria", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("text", metavar="text", help="Inout text of file")

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(args.text)


# --------------------------------------------------
if __name__ == "__main__":
    main()
