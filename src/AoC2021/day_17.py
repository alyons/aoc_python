from typing import List, Tuple


def step(pos: List[int], vel: List[int]):
    pos[0] += vel[0]
    pos[1] += vel[1]

    vel[0] = 0 if not vel[0] else vel[0] - 1
    vel[1] -= 1


def within_target(pos: List[int], target: Tuple[int, int, int, int]) -> bool:
    return pos[0] >= target[0] and pos[0] <= target[1] and pos[1] <= target[2] and pos[1] >= target[3]


def past_target(pos: List[int], target: Tuple[int, int, int, int]) -> bool:
    return pos[0] > target[1] or pos[1] < target[3]


def falls_short(a, b, target) -> bool:
    return a[0] < target[0] and b[0] <= target


def fire(vel: List[int], target: Tuple[int, int, int, int], should_print: bool = False) -> Tuple[bool, int]:
    pos = [0, 0]
    max_y = 0
    _past = False
    _hit = False

    while not _past:
        step(pos, vel)
        if should_print: print(pos)
        max_y = max(max_y, pos[1])
        if (within_target(pos, target)):
            _hit = True
        _past = past_target(pos, target)
    
    return (_hit, max_y)


def sum_consecutive_integers(n: int) -> int:
    return (n * (n + 1))/ 2


def find_max_height(target: Tuple[int, int, int, int]) -> int:

    # Find Max X that doesn't just shoot past the target
    _x = 1
    while sum_consecutive_integers(_x) < target[1]: _x += 1
    
    max_x_vel = _x - 1
    max_y = 0
    max_vel = [max_x_vel, 0]

    # Perform Arch calculations until a shot falls short
    for _base_x in range(max_x_vel, 1, -1):
        _y = 0
        # We should increment y in some fashion
        _hit = True
        while _hit:
            _vel = [_base_x, _y]
            _hit, _max_y = fire(_vel, target)
            print(f'Fire Result [{_base_x}, {_y}]: {_hit}, {_max_y}')
            if _hit and _max_y > max_y:
                max_y = _max_y
                max_vel = [_base_x, _y]
            _y += 1


    return (max_y, max_vel)


def integer_sum(a: int, l: int) -> int:
    n = abs(l) - abs(a) + 1
    return int(n * (a + l) / 2)


def find_slope_and_y_intercept(p0: List[int], p1: List[int]) -> Tuple[int, int]:
    m = (p1[1] - p0[1]) / (p1[0] - p0[0])
    b = p0[1] - m * p0[0]


def find_max_height_ex(target: Tuple[int, int, int, int]) -> int:
    max_y = 0
    max_vel = [0, 0]

    for a in range(1, target[0]):
        for l in range(a + 1, target[1]):
            _sum = integer_sum(a, l)
            if _sum >= target[0] and _sum <= target[1]:
                _hit, _y = fire([a, l], target)
                if _hit and _y > max_y:
                    max_y = _y
                    max_vel = [a, l]
    
    return (max_y, max_vel)


def find_max_height_tlm(target: Tuple[int, int, int, int]) -> int:
    min_x = 0
    max_x = 1

    for n in range(2, target[1]):
        _sum = integer_sum(1, n)
        if _sum > target[0] and _sum < target[1]:
            if not min_x:
                min_x = n

            max_x = max(max_x, n)
    
    max_y = 0
    for x in range(min_x, max_x + 1):
        _first_hit = False
        _second_hit = True
        y = 0
        while not (_first_hit and not _second_hit):
            (hit, y) = fire([x, y], target)
            print(hit, y)
            if hit:
                if not _first_hit: _first_hit = True
                if y > max_y: max_y = y
            elif _first_hit and not hit:
                _second_hit = False
            
            y += 1
    
    print(max_y)


def find_unique_shots(target: Tuple[int, int, int, int]):
    unique = set()

    for x in range(target[0], target[1] + 1):
        for y in range(target[2], target[3] - 1, -1):
            t = (x, y)
            unique.add(t)

    max_y = integer_sum(1, abs(target[3]) - 1)
    min_x = 0
    for n in range(2, target[1]):
        _sum = integer_sum(1, n)
        if _sum > target[0] and _sum < target[1]:
            if not min_x:
                min_x = n
                break
    
    for x in range(min_x, target[1] + 1):
        for y in range(target[3], max_y):
            (hit, _y) = fire([x,y], target)
            if hit:
                unique.add((x, y))

    return len(unique)