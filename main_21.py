from AoC2021.day_21 import get_universes, play_game, propigate_universes, pre_populate_score, get_all_scoring_rolls
from reprint import output


def main():
    print('Welcome to Day 21')

    pos_1 = 4
    pos_2 = 8
    rolls_1 = []
    rolls_2 = []

    result = play_game(pos_1, pos_2)

    print(f'Result: {result}')

    u_1, u_2 = get_universes(pos_1, pos_2, True)
    print(f'Player 1 Wins: {u_1}')
    print(f'Player 2 Wins: {u_2}')


if __name__ == '__main__':
    main()
