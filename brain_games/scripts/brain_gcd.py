#!/usr/bin/env python3


from brain_games.games.brain_gcd_game import get_question_right_answer as game
from brain_games.games.brain_gcd_game import print_task as task
from brain_games.scripts.engine_brain_games import launch_game


def brain_gcd():
    launch_game(task, game)


def main():
    brain_gcd()


if __name__ == '__main__':
    main()
