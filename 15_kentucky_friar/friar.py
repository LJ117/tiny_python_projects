#!/usr/bin/env python3
"""
Author : seven <seven@localhost>
Date   : 2023-07-28
Purpose: Southern fry text
"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Southern fry text",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", help="Input text or file")

    args = parser.parse_args()

    if os.path.isfile(args.text):
        with open(args.text, encoding="utf-8") as text_file:
            args.text = text_file.read().rstrip()

    return args


# --------------------------------------------------
def stemmer(word):
    """split words"""
    pattern = "([aeiou]*)?(ing)(.*)"
    match = re.match(pattern, word)
    if match:
        res1 = match.group(1) or ""
        res2 = match.group(2) or ""
        return (res1, res2)
    else:
        return (word, "")


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for line in str(args.text).splitlines():
        print(line.split())


# --------------------------------------------------
if __name__ == "__main__":
    main()
