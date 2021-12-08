import sys


def align_crabs(crabs: dict) -> int:
    fuel = sys.maxsize
    
    for i in range(max(crabs.keys())):
        temp = _position_cost(crabs, i)
        fuel = min(temp, fuel)

    return fuel


def _position_cost(crabs: dict, position: int) -> int:
    fuel = 0
    for key in crabs:
        fuel += abs(position - key) * crabs[key]
    
    return fuel


def align_crabs_ex(crabs: dict) -> int:
    fuel = sys.maxsize
    travel_cost = {}
    _crab_range = range(max(crabs.keys()) + 1)

    # Calculate travel costs to save time
    for i in _crab_range:
        travel_cost[i] = sum(range(i + 1))

    for i in _crab_range:
        _f = 0
        for key in crabs:
            _t = abs(i - key)
            _f += travel_cost[_t] * crabs[key]
        
        fuel = min(_f, fuel)

    return fuel
