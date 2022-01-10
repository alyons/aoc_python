from concurrent.futures.process import ProcessPoolExecutor
from itertools import repeat
# from tqdm.contrib.concurrent import process_map

from AoC2021.day_21 import scores_from_string, universe_count
from AoCUtils.rich import make_job_progress

from rich.console import Console

console = Console()


def scores_from_string_helper(pos_1: int, pos_2: int, rolls: str) -> tuple[int, int, str]:
    score_1, score_2 = scores_from_string(pos_1, pos_2, rolls)
    return (score_1, score_2, rolls)


def play_quantum_game(pos_1: int, pos_2: int) -> tuple[int, int]:
    universes_1 = 0
    universes_2 = 0

    to_process = [c for c in 'abcdefg']
    job_progress = make_job_progress()
    completed = 0
    running_total = 7
    task_1 = job_progress.add_task('Playing games in the universes', total=running_total)
    min_length = 500
    max_length = -1

    # while to_process:
    #     results = process_map(scores_from_string_helper, repeat(pos_1), repeat(pos_2), to_process, chunksize=max(1, int(len(to_process) / 1000)))
    #     to_process.clear()

    #     for r in results:
    #         score_1, score_2, rolls = r
    #         if score_1 >= 21:
    #             universes_1 += universe_count(rolls)
    #         elif score_2 >= 21:
    #             universes_2 += universe_count(rolls)
    #         else:
    #             to_process.extend([rolls + c for c in 'abcdefg'])

    with console.status(job_progress):
        with ProcessPoolExecutor(max_workers=20) as executor:
            while to_process:
                results = executor.map(scores_from_string_helper, repeat(pos_1), repeat(pos_2), to_process, chunksize=max(1, int(len(to_process) / 1000)))
                to_process.clear()

                for r in results:
                    completed += 1
                    score_1, score_2, rolls = r
                    if score_1 >= 21:
                        universes_1 += universe_count(rolls)
                        if len(rolls) > max_length: max_length = len(rolls)
                        if len(rolls) < min_length: min_length = len(rolls)
                    elif score_2 >= 21:
                        universes_2 += universe_count(rolls)
                        if len(rolls) > max_length: max_length = len(rolls)
                        if len(rolls) < min_length: min_length = len(rolls)
                    else:
                        to_process.extend([rolls + c for c in 'abcdefg'])
                        running_total += 7
        
                job_progress.update(task_1, completed=completed, total=running_total)
        
    console.print(f'Min Length: {min_length}')
    console.print(f'Max Length: {max_length}')

    return (universes_1, universes_2)


def main():
    console.print('Welcome to Day 21 Extreme')

    universes_1, universes_2 = play_quantum_game(3, 10)

    console.print(f'Universe 1: {universes_1}\nUniverse 2: {universes_2}')


if __name__ == '__main__':
    main()
