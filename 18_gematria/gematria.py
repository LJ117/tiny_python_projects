#!/usr/bin/env python3
"""
Author : seven <seven@localhost>
Date   : 2023-08-11
Purpose: Gematria
"""

import argparse
import os
import re
from functools import reduce


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Gematria", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("text", metavar="text", help="Input text of file")
    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def word2num(word):
    vals = map(ord, re.sub("[^a-zA-Z0-9]", "", word))

    word_sum = sum(vals)

    return str(word_sum)


# --------------------------------------------------
def test_word2num():
    """
    Test word2num
    """
    assert word2num("a") == "97"
    assert word2num("abc") == "294"
    assert word2num("ab'c") == "294"
    assert word2num("4a-b'c,") == "346"


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    # for line in str(args.text).splitlines():
    #     print(" ".join(map(word2num, line.split())))

    for line in str(args.text).splitlines():
        new_line = list()
        for word in line.split():
            new_line.append(word2num(word))
        print(" ".join(new_line))


# --------------------------------------------------
if __name__ == "__main__":
    main()
