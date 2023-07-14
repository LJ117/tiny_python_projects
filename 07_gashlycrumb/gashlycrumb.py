#!/usr/bin/env python3
"""
Author : seven <seven@localhost>
Date   : 2023-07-14
Purpose: Gashlycrumb
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Gashlycrumb",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "letter", metavar="letter", nargs="+", type=str, help="Letter(s)"
    )

    parser.add_argument(
        "-f",
        "--file",
        help="Input file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default="gashlycrumb.txt",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    letterDict = dict()
    file = args.file
    for line in file:
        # print(line, end="")
        l_list = line.split()
        letterDict[str(l_list[0]).upper()] = str(line).rstrip()
    file.close()

    letters = args.letter
    for letter in letters:
        letter_key = str(letter).upper()
        if letter_key in letterDict:
            print(letterDict[letter_key])
        else:
            print(f'I do not know "{letter}".')


# --------------------------------------------------
if __name__ == "__main__":
    main()
