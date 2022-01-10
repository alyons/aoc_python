from reprint import output
from time import clock_gettime_ns, CLOCK_REALTIME, sleep

from AoCUtils.utils import sort_string
from AoCUtils.rich import Header, make_default_layout

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

_digits = 'abcdefg'


def potentially_under_score(pos: int, rolls: str) -> bool:
    could_continue = True

    for i in _digits:
        _r = rolls + i
        if score_from_string(pos, _r) >= 21: could_continue = False

    return could_continue


def get_all_scoring_rolls(pos: int, rolls: list[str], base: str = ''):
    _s = score_from_string(pos, base)
    if _s > 20:
        rolls.append(base)
    else:
        for i in _digits:
            _r = base + i
            get_all_scoring_rolls(pos, rolls, _r)


def get_non_scoring_rolls(pos: int, digits: int, rolls: list[str], base: str = ''):
    if len(base) < digits:
        if potentially_under_score(pos, base):
            for i in _digits:
                _r = base + i
                get_non_scoring_rolls(pos, digits, rolls, _r)
    else:
        _s = score_from_string(pos, base)
        if _s < 21: rolls.append(base)
    
    
def get_universes(pos_1: int, pos_2: int, print_debug: bool = False):
    success_1 = []
    success_2 = []

    universes_1 = 0
    universes_2 = 0

    get_all_scoring_rolls(pos_1, success_1)
    get_all_scoring_rolls(pos_2, success_2)

    success_factors_1 = {}
    success_factors_2 = {}

    failure_factors_1 = {}
    failure_factors_2 = {}

    if print_debug: print(f'Create success for pos: {pos_1}...')

    for success in success_1:
        _k = len(success)
        _prod = universe_count(success)
        if not _k in success_factors_1:
            success_factors_1[_k] = {}
        
        if not _prod in success_factors_1[_k]:
            success_factors_1[_k][_prod] = 1
        else:
            success_factors_1[_k][_prod] += 1

    if print_debug: print(f'Completed sucesses for pos: {pos_1}! {len(success_1)}')
    if print_debug: print(f'Create successes for pos: {pos_2}...')
    
    for success in success_2:
        _k = len(success)
        _prod = universe_count(success)
        if not _k in success_factors_2:
            success_factors_2[_k] = {}
        
        if not _prod in success_factors_2[_k]:
            success_factors_2[_k][_prod] = 1
        else:
            success_factors_2[_k][_prod] += 1
    
    if print_debug: print(f'Completed sucesses for pos: {pos_2}! {len(success_2)}')
    if print_debug: print(f'Create failures for pos: {pos_1}...')

    for _s in success_factors_2:
        print(f'Working on length: {_s!r}')
        failure_factors_1[_s] = {}
        _factors = []
        get_non_scoring_rolls(pos_1, _s, _factors)
        for _f in _factors:
            _u = universe_count(_f)
            if not _u in failure_factors_1[_s]:
                failure_factors_1[_s][_u] = 1
            else:
                failure_factors_1[_s][_u] += 1
        _factors.clear()
    
    if print_debug: print(f'Complete failures for pos: {pos_1}!')
    if print_debug: print(f'Create failures for pos: {pos_2}...')
    
    for _s in success_factors_1:
        _l = _s - 1
        print(f'Working on length: {_l!r}')
        failure_factors_2[_l] = {}
        _factors = []
        get_non_scoring_rolls(pos_2, _s - 1, _factors)
        for _f in _factors:
            _u = universe_count(_f)
            if not _u in failure_factors_2[_l]:
                failure_factors_2[_l][_u] = 1
            else:
                failure_factors_2[_l][_u] += 1
        _factors.clear()
    
    if print_debug: print(f'Complete failures for pos: {pos_2}!')

    for _s in success_factors_1:
        _l = _s - 1
        for _k_s in success_factors_1[_s]:
            for _k_f in failure_factors_2[_l]:
                universes_1 += _k_s * success_factors_1[_s][_k_s] * _k_f * failure_factors_2[_l][_k_f]
    
    for _s in success_factors_2:
            _l = _s
            for _k_s in success_factors_2[_s]:
                for _k_f in failure_factors_1[_l]:
                    universes_2 += _k_s * success_factors_2[_s][_k_s] * _k_f * failure_factors_1[_l][_k_f]
            
    return (universes_1, universes_2)
    

def roll_to_chances(roll: str) -> int:
    match roll:
        case 'a': return 1
        case 'b': return 3
        case 'c': return 6
        case 'd': return 7
        case 'e': return 6
        case 'f': return 3
        case 'g': return 1


def distance_to_char(dist:int) -> str:
    match dist:
        case 3: return 'a'
        case 4: return 'b'
        case 5: return 'c'
        case 6: return 'd'
        case 7: return 'e'
        case 8: return 'f'
        case 9: return 'g'


def char_to_distance(c:str) -> int:
    match c:
        case 'a': return 3
        case 'b': return 4
        case 'c': return 5
        case 'd': return 6
        case 'e': return 7
        case 'f': return 8
        case 'g': return 9


def scores_from_string(pos_1: int, pos_2: int, rolls: str) -> tuple[int, int]:
    rolls_1 = rolls[::2]
    rolls_2 = rolls[1::2]

    score_1 = score_from_string(pos_1, rolls_1)
    score_2 = score_from_string(pos_2, rolls_2)

    return (score_1, score_2)


score_dict = {}
def score_from_string(pos: int, rolls: str) -> int:
    k = f'{pos}_{rolls}'
    if k in score_dict: return score_dict[k]

    score = 0

    for i in rolls:
        pos += char_to_distance(i)
        _s = pos % 10
        if not _s: _s = 10
        score += _s
    
    score_dict[k] = score
    
    return score

def pre_populate_score(pos: int, rolls: str = ''):
    pos %= 10
    next_rolls = 'abcdefg'

    _s = score_from_string(pos, rolls)
    if _s < 21:
        for i in next_rolls:
            _r = rolls + i
            pre_populate_score(pos, _r)


universe_dict = {}
def universe_count(rolls: str) -> int:
    k = sort_string(rolls)
    if k in universe_dict: return universe_dict[k]

    universes = 0

    for i in rolls:
        if not universes: universes = 1
        universes *= roll_to_chances(i)

    universe_dict[k] = universes

    return universes


def propigate_universes(pos_1: int, pos_2: int, output_lines, rolls: str = '') -> tuple[int, int]:
    universes_1 = 0
    universes_2 = 0

    roll_values = 'abcdefg'

    output_lines['Roll Value'] = rolls

    score_1, score_2 = scores_from_string(pos_1, pos_2, rolls)
    if score_1 >= 21:
        universes_1 += universe_count(rolls)
        output_lines['Player 1 Wins'] = universes_1
    elif score_2 >= 21:
        universes_2 += universe_count(rolls)
        output_lines['Player 2 Wins'] = universes_2
    else:
        for i in roll_values:
            _r = rolls + i
            _u_1, _u_2 = propigate_universes(pos_1, pos_2, output_lines, _r)
            universes_1 += _u_1
            universes_2 += _u_2

    return (universes_1, universes_2)


class Deterministic_Die():

    def __init__(self):
        self.rolled = 0

    def roll(self) -> int:
        self.rolled += 1
        result = self.rolled % 100
        if not result: result = 100
        return result


def take_turn(pos: int, die: Deterministic_Die) -> tuple[int, int]:
    for _ in range(3):
        pos += die.roll()
    
    _score = pos % 10
    if not _score: _score = 10
    return (pos, _score)


def play_game(pos_1: int, pos_2: int) -> int:
    die = Deterministic_Die()
    turn_p_1 = True
    score_1 = 0
    score_2 = 0

    with output('dict') as output_lines:
        output_lines['Die Rolled'] = die.rolled
        output_lines['Player 1'] = f'Pos: {pos_1:02} Score: {score_1:04}'
        output_lines['Player 2'] = f'Pos: {pos_2:02} Score: {score_2:04}'

        while (score_1 < 1000 and score_2 < 1000):
            if turn_p_1:
                pos_1, _score = take_turn(pos_1, die)
                score_1 += _score
            else:
                pos_2, _score = take_turn(pos_2, die)
                score_2 += _score
            
            turn_p_1 = not turn_p_1

            output_lines['Die Rolled'] = die.rolled
            output_lines['Player 1'] = f'Pos: {pos_1:02} Score: {score_1:04}'
            output_lines['Player 2'] = f'Pos: {pos_2:02} Score: {score_2:04}'
    
    return min(score_1, score_2) * die.rolled
