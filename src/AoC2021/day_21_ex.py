import re
from sys import maxsize
from copy import deepcopy
from time import clock_gettime_ns, CLOCK_REALTIME, sleep
from numpy import prod

from AoCUtils.utils import generate_time_string, manhattan_distance
from AoCUtils.rich import Header, make_default_layout, make_job_progress, make_progress_table, make_variable_panel, make_variable_table

from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.style import Style
from rich.syntax import Syntax
from rich.table import Column, Table
from rich.text import Text

console = Console()
layout = make_default_layout()
layout['header'].update(Header('Dirac Dice [Ex]', 2021, 23))

roll_distance:dict[str, int] = {chr(94 + i):i for i in range(3, 10)}
roll_chance:dict[str, int] = { 'a': 1, 'b': 3, 'c': 6, 'd': 7, 'e': 6, 'f': 3, 'g': 9 }
universe_digits = 'abcdefg'


def score_from_string(pos: int, rolls: str) -> int:
    score = 0
    for r in rolls:
        pos += roll_distance[r]
        _s = pos % 10
        if not _s: _s = 10
        score += 10
    
    return score


def get_all_winning_rolls(pos: int, successes: set[str], base: str = ''):
    score = score_from_string(pos, base)

    if score < 21:
        for d in universe_digits:
            _rolls = base + d
            get_all_winning_rolls(pos, successes, _rolls)
    else:
        successes.add(base)


def generate_losing_rolls(pos: int, digits: int, failures: set, base: str = ''):
    if len(base) < digits:
        for d in universe_digits:
            _rolls = base + d
            generate_losing_rolls(pos, digits, failures, _rolls)
    elif score_from_string(pos, base) < 21:
        failures.add(base)


def universe_count(rolls: str) -> int:
    return prod([roll_chance[r] for r in rolls])


def get_winning_universe_counts(pos_1: int, pos_2: int) -> tuple[int, int]:
    start_time = clock_gettime_ns(CLOCK_REALTIME)
    layout['footer'].update(Panel(generate_time_string(start_time), border_style='green'))
    universes_1 = 0
    universes_2 = 0

    successes_1 = set()
    successes_2 = set()

    failures_1:dict[int, set[str]] = {}
    failures_2:dict[int, set[str]] = {}

    job_progress = make_job_progress()
    gen_s_1 = job_progress.add_task(f'[green]Generate data for Position {pos_1}...', start=False)
    gen_s_2 = job_progress.add_task(f'[green]Generate data for Position {pos_2}...', start=False)
    with console.status(job_progress):
        job_progress.start_task(gen_s_1)
        get_all_winning_rolls(pos_1, successes_1)
        job_progress.update(gen_s_1, total=1, completed=1)
        sleep(1)

        console.print(f'Pos {pos_1} Successes {len(successes_1)}')
        console.print(f'Pos {pos_1} Min Length {len(min(successes_1, key=len))}')
        console.print(f'Pos {pos_1} Max Length {len(max(successes_1, key=len))}')

        job_progress.start_task(gen_s_2)
        get_all_winning_rolls(pos_2, successes_2)
        job_progress.update(gen_s_2, total=1, completed=1)
        sleep(1)

        console.print(f'Pos {pos_2} Successes {len(successes_2)}')
        console.print(f'Pos {pos_2} Min Length {len(min(successes_2, key=len))}')
        console.print(f'Pos {pos_2} Max Length {len(max(successes_2, key=len))}')

        for i in range(len(min(successes_1, key=len)), len(max(successes_1, key=len)) + 1):
            failures_2[i] = set()
            generate_losing_rolls(pos_2, i, failures_2[i])
        sleep(1)
        
        for i in range(len(min(successes_2, key=len)), len(max(successes_2, key=len)) + 1):
            failures_1[i] = set()
            generate_losing_rolls(pos_1, i, failures_1[i])
        sleep(1)
        
        for s in successes_1:
            for f in failures_2[len(s)]:
                universes_1 += universe_count(s + f)

        for s in successes_2:
            for f in failures_1[len(s)]:
                universes_2 += universe_count(s + f)

        console.print(f'Failures[4]: {failures_1.keys()}')

    # layout['footer'].update(Panel('Press enter to quit...', border_style='green'))
    # console.input()

    return (universes_1, universes_2)
