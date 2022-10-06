#!/usr/bin/env python3
from brain_games.games.calc import RULE, generate_qa
import brain_games.engine


def main():
    brain_games.engine.play(RULE, generate_qa)


if __name__ == '__main__':
    main()
