#!/usr/bin/env python3
"""
Author : seven <seven@localhost>
Date   : 2023-07-27
Purpose: Make rhyming "words"
"""

import argparse
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("word", metavar="word", type=str, help="A word to rhyme")

    return parser.parse_args()


# --------------------------------------------------
def test_stemmer():
    """Test stemmer"""
    assert stemmer("") == ("", "")
    assert stemmer("cake") == ("c", "ake")
    assert stemmer("chair") == ("ch", "air")
    assert stemmer("APPLE") == ("", "apple")
    assert stemmer("RDNZL") == ("rdnzl", "")
    assert stemmer("123") == ("123", "")


import string


# --------------------------------------------------
def stemmer(text):
    """Return leading consonants (if any), and 'stem' of word"""

    text = text.lower()

    vowels = "aeiou"
    consonants = "".join([c for c in string.ascii_lowercase if c not in vowels])

    # pattern = f"([{consonants_pattern}]+)?([aeiou])(.*)"
    pattern = "([" + consonants + "]+)?" "([" + vowels + "])" "(.*)"
    match_res = re.match(pattern, text)
    if match_res:
        p1 = match_res.group(1) or ""
        p2 = match_res.group(2) or ""
        p3 = match_res.group(3) or ""
        return (p1, p2 + p3)
    else:
        return (text, "")


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    prefixes = (
        list("bcdfghjklmnpqrstvwxyz")
        + (
            "bl br ch cl cr dr fl fr gl gr pl pr sc "
            "sh sk sl sm sn sp st sw th tr tw thw wh wr "
            "sch scr shr sph spl spr squ str thr"
        ).split()
    )

    word = args.word
    start, reset = stemmer(word)
    if reset:
        print("\n".join(sorted(([p + reset for p in prefixes if p != start]))))
    else:
        print(f'Cannot rhyme "{word}"')


# --------------------------------------------------
if __name__ == "__main__":
    main()
