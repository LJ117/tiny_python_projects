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
            args.text = text_file.read()

    return args


# --------------------------------------------------
def test_fry():
    """Test the func fry()"""
    assert fry("you") == "y'all"
    assert fry("You") == "Y'all"
    assert fry("fishing") == "fishin'"
    assert fry("Aching") == "Achin'"
    assert fry("swing") == "swing"


# --------------------------------------------------
def fry(word):
    """
    Drop the `g` fron `-ing` words, change `you` to `y'all`
    """
    match_you = re.match("([Yy])ou$", word)
    match_ing = re.search("(.+)ing$", word)

    if match_you:
        return match_you.group(1) + "'all"
    elif match_ing:
        prefix = match_ing.group(1)
        if re.search("[aeiouy]", prefix, re.IGNORECASE):
            return prefix + "in'"

    return word


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    splitter = re.compile(r"(\W+)")

    for line in str(args.text).splitlines():
        words = [fry(word) for word in splitter.split(line.rstrip())]
        print("".join(words))


# --------------------------------------------------
if __name__ == "__main__":
    main()
