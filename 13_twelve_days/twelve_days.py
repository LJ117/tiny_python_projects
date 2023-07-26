#!/usr/bin/env python3
"""
Author : seven <seven@localhost>
Date   : 2023-07-26
Purpose: Twelve Days of Christmas
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Twelve Days of Christmas",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-n",
        "--num",
        help="Number of days to sing",
        metavar="days",
        type=int,
        default=12,
    )

    parser.add_argument(
        "-o",
        "--outfile",
        help="Outfile",
        metavar="FILE",
        type=argparse.FileType(mode="wt", encoding="utf-8"),
        default=sys.stdout,
    )
    args = parser.parse_args()
    if not 0 < args.num < 13:
        parser.error(f'--num "{args.num}" must be between 1 and 12')
    return args


# --------------------------------------------------
def test_verse():
    """Test verse"""
    day_one = "\n".join(
        [
            "On the first day of Christmas,",
            "My true love gave to me,",
            "A partridge in a pear tree.",
        ]
    )

    day_two = "\n".join(
        [
            "On the second day of Christmas,",
            "My true love gave to me,",
            "Two turtle doves,",
            "And a partridge in a pear tree.",
        ]
    )
    assert verse(1) == day_one
    assert verse(2) == day_two


# --------------------------------------------------
def verse(day):
    """Generate the verse of Twelve Days"""
    ordinal = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelfth",
    }
    gifts = [
        "A partridge in a pear tree.",
        "Two turtle doves,",
        "Three French hens,",
        "Four calling birds,",
        "Five gold rings,",
        "Six geese a laying,",
        "Seven swans a swimming,",
        "Eight maids a milking,",
        "Nine ladies dancing,",
        "Ten lords a leaping,",
        "Eleven pipers piping,",
        "Twelve drummers drumming,",
    ]

    ret = [f"On the {ordinal[day]} day of Christmas,", "My true love gave to me,"]

    send_gifts = list(reversed(gifts[:day]))

    if day > 1:
        send_gifts[-1] = "And " + send_gifts[-1].lower()

    ret.extend(send_gifts)
    return "\n".join(ret)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    days = args.num
    outfile = args.outfile
    verses = [verse(day) for day in range(1, days + 1)]

    print("\n\n".join(verses), file=outfile)


# --------------------------------------------------
if __name__ == "__main__":
    main()
