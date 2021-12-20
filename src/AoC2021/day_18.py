from math import ceil, floor
from typing import List


class Pair:
    def __init__(self, input: str):
        # Defaults for sanity
        self.left = 0
        self.right = 0
        self.parent = None
        self.is_left = True
        self.depth = 0

        split_index = -1
        bracket_count = 0

        for i, c in enumerate(input):
            if c == '[':
                bracket_count += 1
            elif c == ']':
                bracket_count -= 1

            if bracket_count == 1 and c == ',':
                split_index = i

        _left = input[1:split_index]
        _right = input[split_index + 1:-1]

        if ',' in _left:
            self.left = Pair(_left)
            self.left.set_parent(self)
            self.left._increment_depth()
        else:
            self.left = int(_left)

        if ',' in _right:
            self.right = Pair(_right)
            self.right.is_left = False
            self.right.set_parent(self)
            self.right._increment_depth()
        else:
            self.right = int(_right)
        
    
    def __str__(self):
        return f'[{self.left},{self.right}]'
    
    
    def __add__(self, other):
        _pair = Pair('[0,0]')
        self.set_parent(_pair)
        self.is_left = True
        self._increment_depth()
        other.set_parent(_pair)
        other.is_left = False
        other._increment_depth()
        _pair.left = self
        _pair.right = other
        _pair.reduce()
        return _pair
    

    def _increment_depth(self):
        self.depth += 1
        if isinstance(self.left, Pair): self.left._increment_depth()
        if isinstance(self.right, Pair): self.right._increment_depth()


    def set_parent(self, parent):
        self.parent = parent
    

    def _pass_left(self, value, from_left, caller_depth):
        if caller_depth > self.depth:
            # print(f'L: {self}, value:{value}')
            if from_left:
                if self.parent:
                    self.parent._pass_left(value, self.is_left, self.depth)
            else:
                # print(f'From Left?: {from_left}')
                if isinstance(self.left, Pair):
                    self.left._pass_left(value, self.is_left, self.depth)
                else: # Assume integer
                    # print(f'should be int {self.left}')
                    self.left += value
                    # print(f'Post addition: {self.left}')
        else: # Assume Parent Called
            # print(f'L{self.depth}: A parent called me')
            if isinstance(self.right, Pair):
                self.right._pass_left(value, self.left, self.depth)
            else: # Assume integer
                self.right += value
    

    def _pass_right(self, value, from_right, caller_depth):
        if caller_depth > self.depth:
            # print(f'R{self.depth}: A child called me')
            if from_right:
                if self.parent:
                    self.parent._pass_right(value, not self.is_left, self.depth)
            else:
                if isinstance(self.right, Pair):
                    self.right._pass_right(value, not self.is_left, self.depth)
                else: # Assume integer
                    self.right += value
        else: # Assume Parent Called
            # print(f'R{self.depth}: A parent called me')
            if isinstance(self.left, Pair):
                self.left._pass_right(value, not self.left, caller_depth)
            else: # Assume integer
                self.left += value


    def _explode(self, already_exploded=False):
        if already_exploded: return ()

        explosion = ()
        if self.depth >= 4 and isinstance(self.left, int) and isinstance(self.right, int):
            return (self.left, self.right, self.is_left, self.depth, False)
        if isinstance(self.left, Pair):
            explosion = self.left._explode(already_exploded)
        if not explosion and isinstance(self.right, Pair):
            explosion = self.right._explode(already_exploded)
        if explosion:
            l_value, r_value, from_left, caller_depth, handled = explosion
            if not handled:
                # print(self.data_output())
                self._pass_left(l_value, from_left, caller_depth)
                self._pass_right(r_value, not from_left, caller_depth)
                if from_left:
                    self.left = 0
                else:
                    self.right = 0

                handled = True
            
            return (l_value, r_value, from_left, caller_depth, handled)

        return explosion
    

    def _split(self, already_split=False):
        if already_split: return()

        split = False

        if isinstance(self.left, Pair):
            split = split or self.left._split()
        elif self.left > 9: # Assumes integer
            _l = int(floor(self.left / 2))
            _r = int(ceil(self.left / 2))

            _left = Pair(f'[{_l},{_r}]')
            _left.depth = self.depth + 1
            _left.parent = self
            self.left = _left
            split = True
        
        if isinstance(self.right, Pair):
            split = split or self.right._split()
        elif self.right > 9: # Assumes integer
            _l = int(floor(self.right / 2))
            _r = int(ceil(self.right / 2))

            _right = Pair(f'[{_l},{_r}]')
            _right.depth = self.depth + 1
            _right.parent = self
            _right.is_left = False
            self.right = _right
            split = True

        return split
    
    
    def reduce(self):
        reduce_again = True

        while reduce_again:
            print(self)
            did_explode = bool(self._explode())
            if not did_explode: split = self._split()
            # print(f'Explosion: {explosion} and Split: {split}')
            reduce_again = did_explode or split
    

    def magnitue(self) -> int:
        _l = 1
        _r = 1

        if isinstance(self.left, Pair):
            _l = self.left.magnitue()
        else:
            _l = self.left
        
        if isinstance(self.right, Pair):
            _r = self.right.magnitue()
        else:
            _r = self.right

        return _l * 3 + _r * 2
    
    
    def data_output(self) -> str:
        return f'Depth: {self.depth}\nIs Left: {self.is_left}\nLeft: {self.left}\nRight: {self.right}'
    

    def get_max_depth(self) -> int:
        max_depth = self.depth

        if isinstance(self.left, Pair):
            max_depth = max(max_depth, self.left.get_max_depth())
        
        if isinstance(self.right, Pair):
            max_depth = max(max_depth, self.right.get_max_depth())
        
        return max_depth


    def print_tree(self, lines: List[str] = []):
        print_depth = self.get_max_depth()
        print(print_depth)

        while(print_depth + 3 > len(lines)):
            lines.append('')



def sum_pairs(pairs: List[Pair], print_steps: bool = False) -> Pair:
    pair_sum = None
    for p in pairs:
        if not pair_sum:
            pair_sum = p
        else:
            pair_sum += p
        
        if (print_steps):
            print()
            print(pair_sum)
            print()

    return pair_sum
