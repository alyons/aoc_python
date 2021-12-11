from typing import List
from math import floor

def _tick(grid: List[int]):
    for i in range(len(grid)):
        grid[i] += 1


def _flash(grid: List[int]) -> int:
    should_flash = []
    flashed = []
    check = True

    while check:
        # Process the should_flash octopi
        for s in should_flash:
            neighbors = _get_neighbors(s)
            for n in neighbors:
                grid[n] += 1
            flashed.append(s)
        
        should_flash.clear()

        # Check for which octopi should flash
        for i in range(len(grid)):
            if grid[i] > 9 and not i in flashed:
                should_flash.append(i)
        
        check = bool(should_flash)
    
    # Reset all octopi that flashed
    for f in flashed:
        grid[f] = 0

    return len(flashed)


def _get_neighbors(index: int) -> List[int]:
    neighbors = []

    y = floor(index / 10)
    x = index % 10

    for dY in range(y - 1, y + 2, 1):
        for dX in range(x - 1, x + 2, 1):
            if dX == x and dY == y: continue
            if dX > -1 and dX < 10 and dY > -1 and dY < 10: neighbors.append(10 * dY + dX)

    return neighbors


def flashes_after_steps(grid: List[int], steps: int) -> int:
    flashes = 0

    for s in range(steps):
        _tick(grid)
        flashes += _flash(grid)

    return flashes


def synchro_summon(grid: List[int]) -> int:
    steps = 0

    while not all(g == 0 for g in grid):
        _tick(grid)
        _flash(grid)
        steps += 1

    return steps
