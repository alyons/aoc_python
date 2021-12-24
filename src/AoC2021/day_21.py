class Deterministic_Die():

    def __init__(self):
        self.rolled = 0

    def roll(self) -> int:
        self.rolled += 1
        output = self.rolled % 100
        if not output: output = 100
        return output


def take_turn(pos: int, die: Deterministic_Die) -> int:
    for _ in range(3):
        pos += die.roll()
    
    _score = pos % 10
    if not _score: _score = 10
    return _score


def play_game(pos_1: int, pos_2: int) -> int:
    die = Deterministic_Die()
    turn_p_1 = True
    score_1 = 0
    score_2 = 0

    while (score_1 < 1000 and score_2 < 1000) or die.rolled < 1000:
        if turn_p_1:
            score_1 += take_turn(pos_1, die)
        else:
            score_2 += take_turn(pos_2, die)
        
        turn_p_1 = not turn_p_1
                
    print(f'Die Rolled: {die.rolled}')
