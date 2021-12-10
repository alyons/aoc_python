from typing import List, Tuple
from math import floor


def is_closing(c: str) -> bool:
    return c == ')' or c == ']' or c == '}' or c == '>'


def line_definition(line: str) -> Tuple:
    corruption = -1
    expected = []

    for i, c in enumerate(line):
        if is_closing(c):
            test = expected.pop()
            if c != test:
                corruption = i
                break
        else:
            match c:
                case '(':
                    expected.append(')')
                case '[':
                    expected.append(']')
                case '{':
                    expected.append('}')
                case '<':
                    expected.append('>')

    return (expected, corruption)


def syntax_error_score(lines: List[str]) -> int:
    p = 0 # ()
    k = 0 # []
    c = 0 # {}
    v = 0 # <>

    for l in lines:
        corruption = line_definition(l)[-1]
        if corruption > -1:
            match l[corruption]:
                case ')':
                    p += 1
                case ']':
                    k += 1
                case '}':
                    c += 1
                case '>':
                    v += 1

    return p * 3 + k * 57 + c * 1197 + v * 25137


def middle_score(lines: List[str]) -> int:
    scores = []

    for l in lines:
        expected, corruption = line_definition(l)
        if corruption == -1 and expected:
            score = 0
            while expected:
                e = expected.pop()
                score *= 5
                match e:
                    case ')': score += 1
                    case ']': score += 2
                    case '}': score += 3
                    case '>': score += 4

            if score > 0:
                scores.append(score)
    
    sorted_scores = sorted(scores)
    middle = floor(len(sorted_scores) / 2)

    return sorted_scores[middle]
