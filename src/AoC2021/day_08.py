from typing import List, Tuple


def parse_ssd(input: str) -> Tuple:
    digits = []
    display = []

    halves = input.split('|')
    digits = halves[0].strip().split()
    display = halves[1].strip().split()

    digits = [''.join(sorted(d)) for d in digits]
    display = [''.join(sorted(d)) for d in display]

    return (digits, display)


def is_one(value: str) -> bool:
    return len(value) == 2


def is_seven(value: str) -> bool:
    return len(value) == 3


def is_four(value: str) -> bool:
    return len(value) == 4


def is_eight(value: str) -> bool:
    return len(value) == 7


def is_simple_digit(value: str) -> bool:
    return is_one(value) or is_four(value) or is_seven(value) or is_eight(value)


def count_simple_displays(inputs: List[str]) -> int:
    digit_arrays = []
    display_arrays = []

    for input in inputs:
        _d, _s = parse_ssd(input)
        digit_arrays.append(_d)
        display_arrays.append(_s)
    
    count = 0
    for display in display_arrays:
        count += sum(map(lambda x : is_simple_digit(x), display))
    
    return count


def display_sum(inputs: List[str]) -> int:
    total = 0

    for input in inputs:
        digits, display = parse_ssd(input)
        total += display_value(digits, display)

    return total


def build_digit_dictionary(digits: List[str]) -> dict:
    signals_to_digits = {}
    one_set = {}
    four_set = {}
    seven = ''
    signals = {}

    # Step 1: Find simple digits
    for d in digits:
        if is_one(d):
            signals_to_digits[d] = 1
            one_set = set(d)
        elif is_four(d):
            signals_to_digits[d] = 4
            four_set = set(d)
        elif is_seven(d):
            signals_to_digits[d] = 7
            seven = d
        elif is_eight(d):
            signals_to_digits[d] = 8
    
    # Step 2: Find simple signals
    for s in 'abcdefg':
        test = sum(map(lambda d : s in d, digits))
        if test == 6:
            signals[1] = s
        elif test == 4:
            signals[4] = s
        elif test == 9:
            signals[5] = s
    
    # Step 3: Find Signal 2 & Signal 3
    signals[2] = (one_set - set([signals[5]])).pop()
    signals[3] = (four_set - set([signals[1], signals[2], signals[5]])).pop()

    for d in digits:
        if len(d) == 5: # either 2, 3, or 5
            if all(c in d for c in seven):
                signals_to_digits[d] = 3
            elif signals[4] in d:
                signals_to_digits[d] = 2
            else:
                signals_to_digits[d] = 5
        if len(d) == 6: # either 0, 6, or 9
            if not(signals[3] in d):
                signals_to_digits[d] = 0
            if not(signals[2] in d):
                signals_to_digits[d] = 6
            if not(signals[4] in d):
                signals_to_digits[d] = 9

    return signals_to_digits


def display_value(digits: List[str], display: List[str]) -> int:
    value = 0
    
    signals_to_digits = build_digit_dictionary(digits)
    for i, d in enumerate(display):
        value += signals_to_digits[d] * pow(10, 3 - i)

    return value