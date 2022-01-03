from AoC2021.day_24 import run_program


def test_run_program_input():
    input = [7]
    instructions = [
        'inp w'
    ]
    expected = {
        'w': 7,
        'x': 0,
        'y': 0,
        'z': 0
    }
    actual = { 'w': 0, 'x': 0, 'y': 0, 'z': 0 }
    run_program(instructions, input, actual)
    assert expected == actual

def test_run_program_multiplication():
    input = [7]
    instructions = [
        'inp x',
        'mul x -1'
    ]
    expected = {
        'w': 0,
        'x': -7,
        'y': 0,
        'z': 0
    }
    actual = { 'w': 0, 'x': 0, 'y': 0, 'z': 0 }
    run_program(instructions, input, actual)
    assert expected == actual


def test_run_program_equality():
    input = [3, 9]
    instructions = [
        'inp z',
        'inp x',
        'mul z 3',
        'eql z x'
    ]
    expected = {
        'w': 0,
        'x': 9,
        'y': 0,
        'z': 1
    }
    actual = { 'w': 0, 'x': 0, 'y': 0, 'z': 0 }
    run_program(instructions, input, actual)
    assert expected == actual


def test_run_program_binary():
    input = [15]
    instructions = [
        'inp w',
        'add z w',
        'mod z 2',
        'div w 2',
        'add y w',
        'mod y 2',
        'div w 2',
        'add x w',
        'mod x 2',
        'div w 2',
        'mod w 2'
    ]
    expected = {
        'w': 1,
        'x': 1,
        'y': 1,
        'z': 1
    }
    actual = { 'w': 0, 'x': 0, 'y': 0, 'z': 0 }
    run_program(instructions, input, actual)
    assert expected == actual
