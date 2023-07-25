#!/usr/bin/env python3
"""
Author : seven <seven@localhost>
Date   : 2023-07-25
Purpose: Ransom Note
"""

import argparse
import os
import random


# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Ransom Note",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", help="Input text or file")

    parser.add_argument(
        "-s", "--seed", metavar="int", help="Random seed", type=int, default=None
    )

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def choose(letter):
    """Randomly choose an upper or lowercase letter to return"""

    # return str(letter).lower() if random.choice([True, False]) else str(letter).upper()
    return letter.upper() if random.choice([0, 1]) else letter.lower()


# --------------------------------------------------
def test_choose():
    state = random.getstate()
    random.seed(1)
    assert choose("a") == "a"
    assert choose("b") == "b"
    assert choose("c") == "C"
    assert choose("d") == "d"
    random.setstate(state)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    text = args.text
    # way0 normal for loop
    # ret = ""
    # for t in text:
    #     ret += choose(t)
    # print(ret)

    # way1 list comprehension
    # print("".join([choose(t) for t in text]))

    # way2 map func
    print("".join(map(choose, text)))


# --------------------------------------------------
if __name__ == "__main__":
    main()
