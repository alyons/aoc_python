import re
from copy import deepcopy


class Cuboid:
    def __init__(self, start: tuple[int, int, int], end: tuple[int, int, int], on: bool):
        self.start = start
        self.end = end
        self.on = on
    

    def __str__(self) -> str:
        return f'Start: [{self.start}] End: [{self.end}] On: {self.on}'
    

    def __eq__(self: 'Cuboid', other: 'Cuboid') -> bool:
        return self.start == other.start and self.end == other.end and self.on == other.on
    

    def cubes(self) -> int:
        cubes = 1
        for i in range(3):
            cubes *= abs(self.end[i] - self.start[i]) + 1
        
        return cubes
    

    def get_intersection(self: 'Cuboid', other: 'Cuboid') -> 'Cuboid':
        _start = (
            max(self.start[0], other.start[0]),
            max(self.start[1], other.start[1]),
            max(self.start[2], other.start[2])
        )
        _end = (
            min(self.end[0], other.end[0]),
            min(self.end[1], other.end[1]),
            min(self.end[2], other.end[2])
        )

        return Cuboid(_start, _end, other.on)
    

    def intersects(self: 'Cuboid', other: 'Cuboid') -> bool:
        return (
            (max(self.start[0], other.start[0]) <= min(self.end[0], other.end[0])) and
            (max(self.start[1], other.start[1]) <= min(self.end[1], other.end[1])) and
            (max(self.start[2], other.start[2]) <= min(self.end[2], other.end[2]))
        )
    

    def contains(self: 'Cuboid', other: 'Cuboid') -> bool:
        return (self.start[0] <= other.start[0] and
            self.start[1] <= other.start[1] and
            self.start[2] <= other.start[2] and
            self.end[0] >= other.end[0] and
            self.end[1] >= other.end[1] and
            self.end[2] >= other.end[2])


def parse_reactor_sequence(file: str):
    instructions = []

    cuboid_ptn = re.compile(r'(?P<on>on|off) x=(?P<x0>-?\d+)..(?P<x1>-?\d+),y=(?P<y0>-?\d+)..(?P<y1>-?\d+),z=(?P<z0>-?\d+)..(?P<z1>-?\d+)')

    with open(file) as f:
        for line in f:
            m = cuboid_ptn.match(line.strip())
            if m:
                match_dict = m.groupdict()
                _start = (
                    min(int(match_dict['x0']), int(match_dict['x1'])),
                    min(int(match_dict['y0']), int(match_dict['y1'])),
                    min(int(match_dict['z0']), int(match_dict['z1']))
                )
                _end = (
                    max(int(match_dict['x0']), int(match_dict['x1'])),
                    max(int(match_dict['y0']), int(match_dict['y1'])),
                    max(int(match_dict['z0']), int(match_dict['z1']))
                )
                _on = match_dict['on'] == 'on'

                instructions.append(Cuboid(_start, _end, _on))

    return instructions



def get_cube_difference(a: Cuboid, b: Cuboid) -> list[Cuboid]:
    cuboids = []

    # Calculate values for over and under
    under_x = a.start[0] - b.start[0]
    under_y = a.start[1] - b.start[1]
    under_z = a.start[2] - b.start[2]
    over_x = a.end[0] - b.end[0]
    over_y = a.end[1] - b.end[1]
    over_z = a.end[2] - b.end[2]

    # Calculate X cubes
    if under_x < 0:
        cuboids.append(Cuboid(deepcopy(a.start), (b.start[0] - 1, a.end[1], a.end[2]), a.on))

    if over_x > 0:
        cuboids.append(Cuboid((b.end[0] + 1, a.start[1], a.start[2]), deepcopy(a.end), a.on))
    
    x_min = max(a.start[0], b.start[0])
    x_max = min(a.end[0], b.end[0])

    if under_y < 0:
        cuboids.append(Cuboid((x_min, a.start[1], a.start[2]), (x_max, b.start[1] - 1, a.end[2]), a.on))
    
    if over_y > 0:
        cuboids.append(Cuboid((x_min, b.end[1] + 1, a.start[2]), (x_max, a.end[1], a.end[2]), a.on))
    
    y_min = max(a.start[1], b.start[1])
    y_max = min(a.end[1], b.end[1])

    if under_z < 0:
        cuboids.append(Cuboid((x_min, y_min, a.start[2]), (x_max, y_max, b.start[2] - 1), a.on))
    
    if over_z > 0:
        cuboids.append(Cuboid((x_min, y_min, b.end[2] + 1), (x_max, y_max, a.end[2]), a.on))

    return cuboids


def find_biggest_intersection(test: Cuboid, cuboids: list[Cuboid]) -> Cuboid:
    to_return = None
    max_intersection = 0

    for c in cuboids:
        if test.intersects(c):
            _intersection = test.get_intersection(c)
            if _intersection.cubes() > max_intersection:
                to_return = c
                max_intersection = _intersection.cubes()

    return to_return


def initialize_reactor(instructions: list[Cuboid], is_initialize: bool = True) -> int:
    on_cuboids: list[Cuboid] = []
    validation_cuboid = Cuboid((-50, -50, -50), (50, 50, 50), True)

    for cuboid in instructions:
        if is_initialize and not validation_cuboid.contains(cuboid):
            continue

        if cuboid.on:
            if not on_cuboids:
                on_cuboids.append(cuboid)
            elif all(cuboid.contains(c) for c in on_cuboids):
                on_cuboids.clear()
                on_cuboids.append(cuboid)
            else:
                # print('We need to add only the cubes we don\'t have')
                to_test = [cuboid]
                while to_test:
                    _t = to_test.pop()
                    _c = find_biggest_intersection(_t, on_cuboids)
                    if not _c:
                        on_cuboids.append(_t)
                        print(f'No intersections for {_t}')
                    else:
                        to_test.extend(get_cube_difference(_t, _c))
        else:
            if not on_cuboids:
                print('Everything is already off...')
            elif all(cuboid.contains(c) for c in on_cuboids): # Turn everything off
                on_cuboids.clear()
            else:
                # print('Need to trim all of the on cuboids to make the new set...')
                to_test = [c for c in on_cuboids if c.intersects(cuboid)]
                on_cuboids = [c for c in on_cuboids if not c.intersects(cuboid)]
                while to_test:
                    _t = to_test.pop()
                    on_cuboids.extend(get_cube_difference(_t, cuboid))
        
        # print(f'Current Sum: {sum([cuboid.cubes() for cuboid in on_cuboids])}')

    return sum([cuboid.cubes() for cuboid in on_cuboids])
