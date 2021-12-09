from typing import List, Tuple

def find_low_points(height_map: List[str]) -> List[int]:
    low_points = []

    xMax = len(height_map[0]) - 1
    yMax = len(height_map) - 1

    for y, row in enumerate(height_map):
        for x, point in enumerate(row):
            lowest = True
            if x > 0: # Test Left
                lowest = lowest and point < row[x - 1]
            if x < xMax: # Test Right
                lowest = lowest and point < row[x + 1]
            if y > 0: # Test Up
                lowest = lowest and point < height_map[y - 1][x]
            if y < yMax: # Test Down
                lowest = lowest and point < height_map[y + 1][x]

            if lowest:
                low_points.append(int(point))

    return low_points


def find_low_point_coordinates(height_map: List[str]) -> List[Tuple]:
    low_points = []

    xMax = len(height_map[0]) - 1
    yMax = len(height_map) - 1

    for y, row in enumerate(height_map):
        for x, point in enumerate(row):
            lowest = True
            if x > 0: # Test Left
                lowest = lowest and point < row[x - 1]
            if x < xMax: # Test Right
                lowest = lowest and point < row[x + 1]
            if y > 0: # Test Up
                lowest = lowest and point < height_map[y - 1][x]
            if y < yMax: # Test Down
                lowest = lowest and point < height_map[y + 1][x]

            if lowest:
                low_points.append((int(x), int(y)))

    return low_points


def calculate_risk_level(low_points: List[int]) -> int:
    return sum([x + 1 for x in low_points])


def calculate_basin_size(point: Tuple, height_map: List[str]) -> int:
    basin = []
    peaks = []
    test = [point]
    xMax = len(height_map[0]) - 1
    yMax = len(height_map) - 1

    while len(test) > 0:
        p = test.pop()
        x, y = p
        adjacent = find_adjacent_points(p, xMax, yMax)
        if (height_map[y][x] == '9'):
            peaks.append(p)
        elif not p in basin:
            basin.append(p)
        
        for a in adjacent:
            aX, aY = a
            if (height_map[aY][aX] < '9' and not a in basin and not a in peaks):
                test.append(a)
    
    return len(basin)


def find_adjacent_points(point: Tuple, xMax: int, yMax: int) -> List[Tuple]:
    adjacent = []
    x, y = point

    if x > 0: # Test Left
        adjacent.append((x - 1, y))
    if x < xMax: # Test Right
        adjacent.append((x + 1, y))
    if y > 0: # Test Up
        adjacent.append((x, y - 1))
    if y < yMax: # Test Down
        adjacent.append((x, y + 1))

    return adjacent


def calculate_maximum_basins(height_map: List[str]) -> int:
    low_points = find_low_point_coordinates(height_map)
    basins = [calculate_basin_size(point, height_map) for point in low_points]
    sorted_basins = list(sorted(basins))
    size = 1

    for i in range(-1, -4, -1):
        size *= sorted_basins[i]
    
    return size
