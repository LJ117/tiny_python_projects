#!/usr/bin/env python3
"""
Author : seven <seven@localhost>
Date   : 2023-07-17
Purpose: Apples and bananas
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Apples and bananas",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", help="Input text or file")

    parser.add_argument(
        "-v",
        "--vowel",
        help="The vowel(s) allowed",
        metavar="vowel",
        type=str,
        default="a",
        choices=list("aeiou"),
    )

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    vowel = args.vowel
    new_text = list()

    for char in text:
        if char in "aeiou":
            new_text.append(vowel)
        elif char in "AEIOU":
            new_text.append(str(vowel).upper())
        else:
            new_text.append(char)

    print("".join(new_text))


# --------------------------------------------------
if __name__ == "__main__":
    main()
