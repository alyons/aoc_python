from AoC2019.intcode import execute

def test_execute_basic():
    program = [1,9,10,3,2,3,11,0,99,30,40,50]
    expected = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
    execute(program)
    assert program == expected


def test_execute_two():
    program = [1,1,1,4,99,5,6,0,99]
    expected = [30,1,1,4,2,5,6,0,99]
    execute(program)
    assert program == expected
