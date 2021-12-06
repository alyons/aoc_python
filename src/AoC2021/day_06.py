def _tick(fish_timer:dict):
    zero = fish_timer[0]
    for i in range(1, 9):
        fish_timer[i - 1] = fish_timer[i]
    
    fish_timer[6] += zero
    fish_timer[8] = zero


def lantern_fish_sim(fish_timer: dict, days: int) -> int:
    # Prepopulate items with zeros
    for i in range(9):
        if not i in fish_timer:
            fish_timer[i] = 0
    
    for i in range(days):
        _tick(fish_timer)

    return sum(fish_timer.values())
