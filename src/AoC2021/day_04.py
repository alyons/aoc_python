from typing import List
import sys


def board_score_index(numbers: List[int], board: List[List[int]]) -> int:
    index = sys.maxsize

    for row in board:
        if all(number in numbers for number in row):
            test_index = max([numbers.index(elem) for elem in row])
            index = min(index, test_index)
    
    for i in range(5):
        col = [row[i] for row in board] # Create Columns
        if all(number in numbers for number in col):
            test_index = max([numbers.index(elem) for elem in col])
            index = min(index, test_index)

    return index


def board_score(numbers: List[int], board: List[List[int]]) -> int:
    score = 0
    flat_board = sum(board, []) # Better to build a lambda to make this usable elsewhere https://stackabuse.com/python-how-to-flatten-list-of-lists/
    index = board_score_index(numbers, board)

    if index >= len(numbers): # No appropriate score found
        return 0

    temp = list(filter(lambda item: numbers.index(item) <= index, flat_board))
    score = sum(flat_board) - sum(temp)

    return score


def first_score(numbers: List[int], boards: List[List[List[int]]]) -> int:
    score_index = sys.maxsize
    board_index = -1

    for i, board in enumerate(boards):
        temp_index = board_score_index(numbers, board)
        if temp_index < score_index:
            board_index = i
            score_index = temp_index

    if (board_index == -1 or score_index >= len(numbers)): # never found a scoring board
        return 0

    return numbers[score_index] * board_score(numbers, boards[board_index])

def last_score(numbers: List[int], boards: List[List[List[int]]]) -> int:
    score_index = -1
    board_index = -1

    for i, board in enumerate(boards):
        temp_index = board_score_index(numbers, board)
        if temp_index > score_index:
            board_index = i
            score_index = temp_index

    if (board_index == -1 or score_index >= len(numbers)): # never found a scoring board
        return 0

    return numbers[score_index] * board_score(numbers, boards[board_index])
