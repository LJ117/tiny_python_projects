#!/usr/bin/env python3
"""
Author : seven <seven@localhost>
Date   : 2023-08-07
Purpose: Mad Libs
"""

import argparse
import re
import sys
from pprint import pprint


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Mad Libs", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "file", metavar="FILE", type=argparse.FileType("rt"), help="Input file"
    )

    parser.add_argument(
        "-i",
        "--inputs",
        help="Inputs (for testing)",
        metavar="input",
        type=str,
        nargs="*",
        default=None,
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    inputs = args.inputs
    text = args.file.read().rstrip()
    filename = args.file.name
    blanks = re.findall("(<(.*?)>)", text)
    if not blanks:
        sys.exit(f'"{filename}" has no placeholders.')

    tmpl = "Give me {} {}:"
    for placeholder, pos in blanks:
        article = "an" if pos.lower()[0] in "aeiou" else "a"
        answer = inputs.pop(0) if inputs else input(tmpl.format(article, pos))
        text = re.sub(placeholder, answer, text, count=1)

    print(text)


# --------------------------------------------------
if __name__ == "__main__":
    main()
