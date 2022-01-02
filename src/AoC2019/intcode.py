from time import sleep

from AoCUtils.rich import Header, make_default_layout

from rich.live import Live
from rich.panel import Panel
from rich.table import Table


def make_function_panel(data: list[tuple[str, str]]) -> Panel:
    grid = Table.grid(expand=True)
    grid.add_column('Name')
    grid.add_column('Value')

    for datum in data:
        grid.add_row(*datum)

    return Panel(
        grid,
        title='Memory Updates',
        border_style='Green'
    )


def addition(program: list[int], index: int) -> int:
    a_index = program[index + 1]
    b_index = program[index + 2]
    sum_index = program[index + 3]
    program[sum_index] = program[a_index] + program[b_index]

    data = [
        ('Function', 'Addition'),
        ('Index', f'{index}'),
        (f'A[{a_index}]', f'{program[a_index]}'),
        (f'B[{b_index}]', f'{program[b_index]}'),
        (f'Sum[{sum_index}]', f'{program[sum_index]}'),
    ]

    layout['variables'].update(make_function_panel(data))

    return index + 4


def multiplication(program: list[int], index: int) -> int:
    a_index = program[index + 1]
    b_index = program[index + 2]
    sum_index = program[index + 3]
    program[sum_index] = program[a_index] * program[b_index]

    data = [
        ('Function', 'Multiplication'),
        ('Index', f'{index}'),
        (f'A[{a_index}]', f'{program[a_index]}'),
        (f'B[{b_index}]', f'{program[b_index]}'),
        (f'Product[{sum_index}]', f'{program[sum_index]}'),
    ]

    layout['variables'].update(make_function_panel(data))

    return index + 4


def operate(program: list[int], index: int) -> int:
    match program[index]:
        case 1:
            return addition(program, index)
        case 2:
            return multiplication(program, index)
        case 99:
            return index
        # case _:
        #     return index


layout = make_default_layout()
layout['header'].update(Header('Intcode', 2019, 2))


def execute(program: list[int], index: int = 0, run_slow: int = 0) -> int:
    should_operate = True

    if run_slow:
        with Live(layout, screen=True):
            while should_operate:
                index = operate(program, index)
                sleep(run_slow)
                should_operate = program[index] != 99
    else:
        while should_operate:
            index = operate(program, index)
            sleep(run_slow)
            should_operate = program[index] != 99
    
    return index
