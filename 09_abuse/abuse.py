#!/usr/bin/env python3
"""
Author : seven <seven@localhost>
Date   : 2023-07-18
Purpose: Heap abuse
"""

import argparse
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Heap abuse",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-a",
        "--adjectives",
        help="Number of adjectives",
        metavar="adjectives",
        type=int,
        default=2,
    )

    parser.add_argument(
        "-n",
        "--number",
        help="Number of insults",
        metavar="insults",
        type=int,
        default=3,
    )

    parser.add_argument(
        "-s",
        "--seed",
        help="Random seed",
        metavar="seed",
        type=int,
    )
    args = parser.parse_args()

    # check the negative number
    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')
    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    adjective_num = args.adjectives
    lines = args.number

    adjectives = """
    bankrupt base caterwauling corrupt cullionly detestable dishonest false
    filthsome filthy foolish foul gross heedless indistinguishable infected
    insatiate irksome lascivious lecherous loathsome lubbery old peevish
    rascaly rotten ruinous scurilous scurvy slanderous sodden-witted
    thin-faced toad-spotted unmannered vile wall-eyed
    """.strip().split()

    nouns = """
    Judas Satan ape ass barbermonger beggar block boy braggart butt
    carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool
    gull harpy jack jolthead knave liar lunatic maw milksop minion
    ratcatcher recreant rogue scold slave swine traitor varlet villain worm
    """.strip().split()

    # only range the number, so use '_' to disregard
    for _ in range(lines):
        insult = "You "
        adj_list = random.sample(population=adjectives, k=adjective_num)
        noun = random.choice(nouns)
        insult = insult + ", ".join(adj_list)
        print(f"{insult} {noun}!")


# --------------------------------------------------
if __name__ == "__main__":
    main()
