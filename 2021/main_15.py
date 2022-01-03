from AoC2021.day_15_ex import bigger_cave_score, bigger_chiton_a_star, bigger_rich_cave_render, bigger_risk_score, chiton_a_star, parse_chiton_cave, rich_cave_render, risk_score

from rich.console import Console

console = Console()

def main():
    console.print('Welcome to Day 15 EX of Advent of Code 2021')

    cave = parse_chiton_cave('./tests/data/day_15.txt')
    # path = chiton_a_star(cave)

    # for text in rich_cave_render(cave, path):
    #     console.print(text)
    
    # console.print()
    # console.print(f'Risk Score: {risk_score(cave, path)}')

    bigger_path = bigger_chiton_a_star(cave)


    for text in bigger_rich_cave_render(cave, bigger_path):
        console.print(text)

    console.print(f'Bigger Risk Score: {bigger_risk_score(cave, bigger_path)}')

if __name__ == '__main__':
    main()
