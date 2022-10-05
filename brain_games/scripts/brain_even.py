#!/usr/bin/env python3
import brain_games.func


def main():
    name = brain_games.func.welcome_user()
    brain_games.func.play(name)


if __name__ == '__main__':
    main()
