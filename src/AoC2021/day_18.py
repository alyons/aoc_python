from math import floor, ceil
import re


def _is_digit(character: str) -> bool:
    return character in '1234567890'


def _addition(a: str, b: str) -> str:
    return f'[{a},{b}]'


def _explosion_index(sf_number: str) -> int:
    depth = 0

    for i, d in enumerate(sf_number):
        depth += 1 if d == '[' else -1 if d == ']' else 0
        if depth > 4: return i

    return -1


def _explode(sf_number: str, index: int) -> str:
    # Get numbers
    number_index = index + 1
    first_str = ''
    for i in range(number_index, len(sf_number)):
        if _is_digit(sf_number[i]):
            first_str += sf_number[i]
        else:
            number_index = i + 1
            break
    
    second_str = ''
    for i in range(number_index, len(sf_number)):
        if _is_digit(sf_number[i]):
            second_str += sf_number[i]
        else:
            number_index = i + 1
            break
    
    # Process Left Side
    left = sf_number[:index]
    left_number = int(first_str)
    left_index = -1
    for i in range(len(left) - 1, -1, -1):
        if _is_digit(left[i]) and left_index < 0:
            left_index = i
        elif not _is_digit(left[i]) and left_index > -1:
            other_number = left[i+1:left_index+1]
            left_number += int(other_number)
            left = left[:i+1] + str(left_number) + left[left_index+1:] 
            break

    # Process Right Side
    right = sf_number[number_index:]
    right_number = int(second_str)
    right_index = -1
    for i in range(0, len(right)):
        if _is_digit(right[i]) and right_index < 0:
            right_index = i
        elif not _is_digit(right[i]) and right_index > -1:
            other_number = right[right_index: i]
            right_number += int(other_number)
            right = right[:right_index] + str(right_number) + right[i:] 
            break

    return f'{left}0{right}'

def _split_index(sf_number: str) -> int:
    potential_index = -1

    for i, d in enumerate(sf_number):
        if _is_digit(d):
            if potential_index == -1:
                potential_index = i
            else:
                return potential_index
        else:
            potential_index = -1

    return -1


def _split(sf_number: str, index: int) -> str:
    end = index - 1
    for i in range(index, len(sf_number)):
        end += 1
        if not _is_digit(sf_number[i]):
            break
    to_split = int(sf_number[index:end])
    return f'{sf_number[:index]}[{int(floor(to_split / 2))},{int(ceil(to_split / 2))}]{sf_number[end:]}'


def _reduce(sf_number: str) -> tuple[bool, str]:
    did_reduce = False

    e_i = _explosion_index(sf_number)
    if e_i > -1:
        sf_number = _explode(sf_number, e_i)
        did_reduce = True
    
    if not did_reduce:
        s_i = _split_index(sf_number)
        if s_i > -1:
            sf_number = _split(sf_number, s_i)
            did_reduce = True

    return (did_reduce, sf_number)


def snailfish_addition(elements: list[str]) -> str:
    value = None

    for e in elements:
        if not value:
            value = e
        else:
            value = _addition(value, e)
            did_reduce, value = _reduce(value)
            while did_reduce:
                did_reduce, value = _reduce(value)

    return value

def _magnitude_replace(match: re.Match):
    left = int(match.group(1)) * 3
    right = int(match.group(2)) * 2
    return str(left + right)


def magnitude(sf_number: str) -> int:
    while '[' in sf_number:
        sf_number = re.sub(r'\[(\d+),(\d+)\]', _magnitude_replace, sf_number)
        
    return int(sf_number)


def find_largest_pair_magnitude(elements: list[str]) -> int:
    mag = 0

    for i in range(len(elements) - 1):
        for j in range(i + 1, len(elements)):
            _m = magnitude(snailfish_addition([elements[i], elements[j]]))
            if _m > mag: mag = _m
            _m = magnitude(snailfish_addition([elements[j], elements[i]]))
            if _m > mag: mag = _m

    return mag
