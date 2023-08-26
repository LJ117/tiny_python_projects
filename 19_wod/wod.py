#!/usr/bin/env python3
"""
Author : seven <seven@localhost>
Date   : 2023-08-16
Purpose: Create Workout of (the) Day (WOD)
"""

import argparse
import random
import io
import csv
import re
from pprint import pprint
from tabulate import tabulate


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Create Workout of (the) Day (WOD)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-f",
        "--file",
        help="CSV input file of exercises",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default="inputs/exercises.csv",
    )

    parser.add_argument(
        "-s",
        "--seed",
        help="Random seed",
        metavar="seed",
        type=int,
        default=None,
    )

    parser.add_argument(
        "-n",
        "--num",
        help="Number of exercises",
        metavar="exercises",
        type=int,
        default=4,
    )

    parser.add_argument("-e", "--easy", help="Halve the reps", action="store_true")
    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def test_read_csv():
    """
    Test the function read_csv()
    """
    text = io.StringIO("exercise,reps\nBurpees,20-50\nSitups,40-100\n")
    assert read_csv(text) == [("Burpees", 20, 50), ("Situps", 40, 100)]


# --------------------------------------------------
def read_digits(text):
    pattern = r"(\d+)-(\d+)"
    match = re.match(pattern, text)
    if match:
        low, hight = match.groups()
        return int(low), int(hight)
    return (0, 0)


# --------------------------------------------------
def read_csv(fh):
    """
    Read the CSV input
    """
    reader = csv.DictReader(fh, delimiter=",")
    exercise = list()
    for row in reader:
        name, reps = row["exercise"], row["reps"]
        low, high = read_digits(reps)
        exercise.append((name, low, high))
    return exercise


# --------------------------------------------------
def main():
    args = get_args()
    random.seed(args.seed)
    wod = []
    exercises = read_csv(args.file)

    for name, low, high in random.sample(exercises, k=args.num):
        reps = random.randint(low, high)
        if args.easy:
            reps = int(reps / 2)
        wod.append((name, reps))

    print(tabulate(wod, headers=["Exercise", "Reps"]))


# --------------------------------------------------
if __name__ == "__main__":
    main()
