from AoC2021.day_18 import find_largest_pair_magnitude, magnitude, snailfish_addition
from AoC2021.util import parse_file


def test_snailfish_addition_basic():
    inputs = ['[1,2]', '[[3,4],5]']
    expected = '[[1,2],[[3,4],5]]'
    actual = snailfish_addition(inputs)
    assert expected == actual


def test_snailfish_addition_novice():
    inputs = ['[[[[4,3],4],4],[7,[[8,4],9]]]','[1,1]']
    expected = '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'
    actual = snailfish_addition(inputs)
    assert expected == actual


def test_snailfish_addition_adept():
    inputs = ['[1,1]', '[2,2]', '[3,3]', '[4,4]', '[5,5]', '[6,6]']
    expected = '[[[[5,0],[7,4]],[5,5]],[6,6]]'
    actual = snailfish_addition(inputs)
    assert expected == actual


def test_snailfish_addition_expert():
    inputs = ['[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]', '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]', '[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]', '[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]', '[7,[5,[[3,8],[1,4]]]]', '[[2,[2,2]],[8,[8,1]]]', '[2,9]', '[1,[[[9,3],9],[[9,0],[0,7]]]]', '[[[5,[7,4]],7],1]', '[[[[4,2],2],6],[8,7]]']
    expected = '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'
    actual = snailfish_addition(inputs)
    assert expected == actual


def test_magnitude_basic():
    inputs = '[[1,2],[[3,4],5]]'
    expected = 143
    actual = magnitude(inputs)
    assert expected == actual


def test_snailfish_savage():
    inputs = ['[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]', '[[[5,[2,8]],4],[5,[[9,9],0]]]', '[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]', '[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]', '[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]', '[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]', '[[[[5,4],[7,7]],8],[[8,3],8]]', '[[9,3],[[9,9],[6,[4,9]]]]', '[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]', '[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]']
    e_sum = '[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]'
    a_sum = snailfish_addition(inputs)
    assert e_sum == a_sum
    e_mag = 4140
    a_mag = magnitude(a_sum)
    assert e_mag == a_mag


def test_find_largest_pair_magnitude():
    inputs = parse_file('./tests/data/day_18.txt')
    expected = 3993
    actual = find_largest_pair_magnitude(inputs)
    assert expected == actual
