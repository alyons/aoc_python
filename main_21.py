from AoC2021.day_21 import get_universes, play_game


def main():
    print('Welcome to Day 21')

    pos_1 = 4  # 444356092776315
    pos_2 = 8  # 341960390180808
    # pos_1 = 3    # 132798212100
    # pos_2 = 10   # 56073004758

    result = play_game(pos_1, pos_2)

    print(f'Result: {result}')

    u_1, u_2 = get_universes(pos_1, pos_2, True)
    print(f'Player 1 Wins: {u_1}')
    print(f'Player 2 Wins: {u_2}')


if __name__ == '__main__':
    main()
