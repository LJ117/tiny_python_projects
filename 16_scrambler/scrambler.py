#!/usr/bin/env python3
"""
Author : seven <seven@localhost>
Date   : 2023-08-02
Purpose: Scramble the letters of words
"""

import argparse
import os
import random
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Scramble the letters of words",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", help="Input text or file")

    parser.add_argument(
        "-s",
        "--seed",
        help="Random seed",
        metavar="seed",
        type=int,
        default=None,
    )

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def test_scramble():
    """
    Test the scrambler func
    """
    state = random.getstate()

    random.seed(1)

    # assert scramble("a") == "a"
    # assert scramble("ab") == "ab"
    # assert scramble("abc") == "abc"
    # assert scramble("abcd") == "acbd"
    # assert scramble("abcde") == "acbde"
    # assert scramble("abcdef") == "aecbdf"
    # assert scramble("abcde'f") == "abcd'ef"
    assert scramble("foobar") == "faobor"

    random.setstate(state)


# --------------------------------------------------
def scramble(word):
    """
    Scrambler a word:
    1. If the word is three characters or shorter, return the word unchanged
    2. Use a string slice to copy the characters, not including the first and last.
    3. Use the random.shuffle() method to mix up the letters in the middle.
    4. Return the new "word" by combining the first, middle, and last parts
    """
    # re.match(r"\w+", word) 确保里面有character, 有字符可以用于交换；
    # 换言之，空格或者换行符 直接原样返回
    if len(word) > 3 and re.match(r"\w+", word):
        middle = list(word[1:-1])
        random.shuffle(middle)
        word = word[0] + "".join(middle) + word[-1]

    return word


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()

    random.seed(args.seed)

    ret = []

    splitter = re.compile("([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")

    # for line in args.text.splitlines():
    #     ret_line = []
    #     for word in splitter.split(line):
    #         ret_line.append(scramble(word))
    #     ret.append("".join(ret_line))
    # print("\n".join(ret))

    # for line in str(args.text).splitlines():
    #     print("".join([scramble(word) for word in splitter.split(line)]))

    for line in str(args.text).splitlines():
        print("".join(map(scramble, splitter.split(line))))


# --------------------------------------------------
if __name__ == "__main__":
    main()
