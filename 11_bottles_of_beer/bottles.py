#!/usr/bin/env python3
"""
Author : seven <seven@localhost>
Date   : 2023-07-21
Purpose: Bottle of beer song
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Bottle of beer song",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-n",
        "--num",
        help="How many bottles",
        metavar="number",
        type=int,
        default=10,
    )

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


def verse(bottle):
    """Sing a verse"""
    next_bottle = bottle - 1
    s1 = "" if bottle == 1 else "s"
    s2 = "" if next_bottle == 1 else "s"
    num_text = "No more" if next_bottle == 0 else next_bottle

    return "\n".join(
        [
            f"{bottle} bottle{s1} of beer on the wall,",
            f"{bottle} bottle{s1} of beer,",
            "Take one down, pass it around,",
            f"{num_text} bottle{s2} of beer on the wall!",
        ]
    )


def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == "\n".join(
        [
            "1 bottle of beer on the wall,",
            "1 bottle of beer,",
            "Take one down, pass it around,",
            "No more bottles of beer on the wall!",
        ]
    )

    two_verse = verse(2)
    assert two_verse == "\n".join(
        [
            "2 bottles of beer on the wall,",
            "2 bottles of beer,",
            "Take one down, pass it around,",
            "1 bottle of beer on the wall!",
        ]
    )


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    int_arg = args.num
    print("\n\n".join(map(verse, range(int_arg, 0, -1))))


# --------------------------------------------------
if __name__ == "__main__":
    main()
