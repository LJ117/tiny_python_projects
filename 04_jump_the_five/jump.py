#!/usr/bin/env python3
"""
Author : seven <seven@localhost>
Date   : 2023-07-07
Purpose: Jump the five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Jump the five",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="str", help="Input text")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    jumper = {
        "1": "9",
        "9": "1",
        "2": "8",
        "8": "2",
        "3": "7",
        "7": "3",
        "4": "6",
        "6": "4",
        "5": "0",
        "0": "5",
    }

    for char in args.text:
        print(jumper.get(char, char), end="")

    print()


# --------------------------------------------------
if __name__ == "__main__":
    main()
