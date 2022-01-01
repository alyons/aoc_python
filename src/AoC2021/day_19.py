from copy import deepcopy
from tqdm import tqdm

###################################################
#                   Rotation Table                #
#       X Axis          Y Axis          Z Axis    #
# 0 | x | y | z |   | x | y | z |   | x | y | z | #
# 1 | x | z |-y |   |-z | y | x |   | y |-x | z | #
# 2 | x |-y |-z |   |-x | y |-z |   |-x |-y | z | #
# 3 | x |-z | y |   | z | y |-x |   |-y | x | z | #
###################################################

def apply_clockwise_rotation(beacon: list[int], rotation: list[int], print_debug: bool = False):
    if print_debug: print(f'Rotating [X,Y,Z]: {rotation}')
    for _ in range(rotation[0]): # Rotate via X Axis
        _y = beacon[2]
        _z = -beacon[1]
        beacon[1] = _y
        beacon[2] = _z
        if print_debug: print(f'After X Rot: {beacon}')
    
    for _ in range(rotation[1]): # Rotate via Y Axis
        _x = -beacon[2]
        _z = beacon[0]
        beacon[0] = _x
        beacon[2] = _z
        if print_debug: print(f'After Y Rot: {beacon}')

    for _ in range(rotation[2]): # Rotate via Z Axis
        _x = beacon[1]
        _y = -beacon[0]
        beacon[0] = _x
        beacon[1] = _y
        if print_debug: print(f'After Z Rot: {beacon}')


def add_beacon_offset(beacon: list[int], offset: list[int]):
    beacon[0] += offset[0]
    beacon[1] += offset[1]
    beacon[2] += offset[2]


def subtract_beacon_offset(beacon: list[int], offset: list[int]):
    beacon[0] -= offset[0]
    beacon[1] -= offset[1]
    beacon[2] -= offset[2]


class Scanner:
    def __init__(self, beacons: list[list[int]]):
        self.beacons = beacons
        self.position = [0, 0, 0]
        self.rotation = [0, 0, 0]
        self.reference_rotations = []
        self.locked = False
    

    def __str__(self):
        return f'Scanner -> [{self.position}] ({self.rotation}) |{self.reference_rotations}|'


    # Rotate along the X Axis
    def rotate_x_axis(self):
        if not self.locked:
            self.rotation[0] += 1
            if self.rotation[0] > 3: self.rotation[0] = 0
            for beacon in self.beacons:
                apply_clockwise_rotation(beacon, [1,0,0])
    

    # Rotate along the Y Axis
    def rotate_y_axis(self):
        if not self.locked:
            self.rotation[1] += 1
            if self.rotation[1] > 3: self.rotation[1] = 0
            for beacon in self.beacons:
                apply_clockwise_rotation(beacon, [0,1,0])
    

    # Rotation along the Z Axis
    def rotate_z_axis(self):
        if not self.locked:
            self.rotation[2] += 1
            if self.rotation[2] > 3: self.rotation[2] = 0
            for beacon in self.beacons:
                apply_clockwise_rotation(beacon, [0,0,1])


    # Create Beacon set
    def create_beacon_set(self: 'Scanner', adjustment: list[int]) -> set[tuple[int, int, int]]:
        return {(b[0] - adjustment[0], b[1] - adjustment[1], b[2] - adjustment[2]) for b in self.beacons}

    
    def get_absolute_beacon_set(self: 'Scanner') -> set[tuple[int, int, int]]:
        _beacons = set()

        for b in self.beacons:
            _b = b.copy()
            add_beacon_offset(_b, self.position)
            _beacons.add(tuple(_b))

        return _beacons


    # Find overlap area for two scanners
    def overlap(scanner_a: 'Scanner', scanner_b: 'Scanner', print_debug: bool = False) -> bool:
        found = False
        beacon_a = None
        beacon_b = None
        a_index = -1
        b_index = -1

        for beacon_a in scanner_a.beacons:
            rel_beacons_a = scanner_a.create_beacon_set(beacon_a)
            for _ in range(4):
                for _ in range(4):
                    for _ in range(4):
                        for beacon_b in scanner_b.beacons:
                            rel_beacons_b = scanner_b.create_beacon_set(beacon_b)
                            shared = rel_beacons_a.intersection(rel_beacons_b)
                            if len(shared) >= 12:
                                _s = shared.pop()
                                relative_a = [_s[0] + beacon_a[0], _s[1] + beacon_a[1], _s[2] + beacon_a[2]]
                                relative_b = [_s[0] + beacon_b[0], _s[1] + beacon_b[1], _s[2] + beacon_b[2]]
                                a_index = scanner_a.beacons.index(relative_a)
                                b_index = scanner_b.beacons.index(relative_b)
                                if (print_debug): print(f'Scanner A Pos: {scanner_a.position}')
                                if (print_debug): print(f'Scanner A: {scanner_a.beacons[a_index]}')
                                if (print_debug): print(f'Scanner B: {scanner_b.beacons[b_index]}')
                                found = True
                        
                        if found: break
                        scanner_b.rotate_z_axis()
                    
                    if found: break
                    scanner_b.rotate_y_axis()
                
                if found: break
                scanner_b.rotate_x_axis()
            
            if found: break
        
        # Process and set Scanner B appropriately
        if found:
            # Set Rotations and reference rotations
            scanner_b.reference_rotations = deepcopy(scanner_a.reference_rotations)
            if scanner_a.rotation != [0, 0, 0]: scanner_b.reference_rotations.append(deepcopy(scanner_a.rotation))
            
            # Apply logical distance between spaces
            beacon_a = scanner_a.beacons[a_index]
            beacon_b = scanner_b.beacons[b_index]
            if print_debug: print(f'A: {beacon_a} - B: {beacon_b}')
            distance = deepcopy(beacon_a)
            subtract_beacon_offset(distance, beacon_b)
            if print_debug: print(f'Distance: {distance}')
            add_beacon_offset(scanner_b.position, scanner_a.position)
            add_beacon_offset(scanner_b.position, distance)

            if (print_debug): print(f'Scanner B New Position: {scanner_b.position}')
            scanner_b.locked = True

        return found
        

def parse_scanners(file: str) -> list[Scanner]:
    scanners: list[Scanner] = []
    beacons: list[int] = []
    with open(file) as f:
        for line in f:
            if 'scanner' in line and beacons:
                scanners.append(Scanner(sorted(beacons.copy(), key = lambda x: (x[0], x[1], x[2]))))
                beacons.clear()
            elif ',' in line:
                beacons.append([int(c) for c in line.strip().split(',')])

    if beacons:
        scanners.append(Scanner(beacons.copy()))

    scanners[0].locked = True
    return scanners


def build_beacon_map(scanners: list[Scanner]) -> set[tuple[int, int, int]]:
    scanner_range = range(len(scanners))
    position_dict: dict[int, int] = {}
    
    progress = tqdm(len(scanners))

    while any(not s.locked for s in scanners):
        for i in scanner_range:
            for j in scanner_range:
                if i == j:
                    # print('Cannot overlap a scanner with itself...')
                    continue
                elif scanners[i].locked ^ scanners[j].locked:
                    if scanners[i].locked:
                        if scanners[i].overlap(scanners[j], False):
                            progress.update(1)
                            position_dict[j] = i
                    else:
                        if scanners[j].locked:
                            if scanners[j].overlap(scanners[i], False):
                                progress.update(1)
                                position_dict[i] = j
                else:
                    # print('Both scanners are in the same state, so can not compare...')
                    continue  
    progress.close()

    beacons = set()
    for s in scanners: beacons |= s.get_absolute_beacon_set()
    return beacons


def manhattan_distance(a: list[int], b: list[int]):
    distance = 0
    for i in range(0, 3):
        distance += abs(a[i] - b[i])
    
    return distance


def largest_distance_between_scanners(scanners: list[Scanner]) -> int:
    max_distance = 0

    for i in range(0, len(scanners) - 1):
        for j in range(i + 1, len(scanners)):
            distance = manhattan_distance(scanners[i].position, scanners[j].position)
            if distance > max_distance: max_distance = distance
    
    return max_distance
