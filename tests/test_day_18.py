from AoC2021.day_18 import Pair, sum_pairs
from AoC2021.util import parse_file


def test_pair_reduce():
    expected = {
        'a': '[[[[0,9],2],3],4]',
        'b': '[7,[6,[5,[7,0]]]]',
        'c': '[[6,[5,[7,0]]],3]',
        'd': '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'
    }
    actual = {}
    a = Pair('[[[[[9,8],1],2],3],4]')
    a.reduce()
    actual['a'] = a.__str__()

    b = Pair('[7,[6,[5,[4,[3,2]]]]]')
    b.reduce()
    actual['b'] = b.__str__()

    c = Pair('[[6,[5,[4,[3,2]]]],1]')
    c.reduce()
    actual['c'] = c.__str__()

    d = Pair('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]')
    d.reduce()
    actual['d'] = d.__str__()

    assert expected == actual


def test_pair_add():
    expected = Pair('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')
    a = Pair('[[[[4,3],4],4],[7,[[8,4],9]]]')
    b = Pair('[1,1]')
    actual = a + b
    assert str(expected) == str(actual)


def test_pair_sum_a():
    pair_strings = ['[1,1]', '[2,2]', '[3,3]', '[4,4]']
    pairs = [Pair(p) for p in pair_strings]
    actual = sum_pairs(pairs)
    expected = Pair('[[[[1,1],[2,2]],[3,3]],[4,4]]')
    assert str(expected) == str(actual)


def test_pair_sum_b():
    pair_strings = ['[1,1]', '[2,2]', '[3,3]', '[4,4]', '[5,5]']
    pairs = [Pair(p) for p in pair_strings]
    actual = sum_pairs(pairs)
    expected = Pair('[[[[3,0],[5,3]],[4,4]],[5,5]]')
    assert str(expected) == str(actual)


def test_pair_sum_c():
    pair_strings = ['[1,1]', '[2,2]', '[3,3]', '[4,4]', '[5,5]', '[6,6]']
    pairs = [Pair(p) for p in pair_strings]
    actual = sum_pairs(pairs)
    expected = Pair('[[[[5,0],[7,4]],[5,5]],[6,6]]')
    assert str(expected) == str(actual)


def test_pair_sum_d():
    pair_strings = [
        '[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]',
        '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]',
        '[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]',
        # '[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]',
        # '[7,[5,[[3,8],[1,4]]]]',
        # '[[2,[2,2]],[8,[8,1]]]',
        # '[2,9]',
        # '[1,[[[9,3],9],[[9,0],[0,7]]]]',
        # '[[[5,[7,4]],7],1]',
        # '[[[[4,2],2],6],[8,7]]'
    ]
    pairs = [Pair(p) for p in pair_strings]
    actual = sum_pairs(pairs, True)
    expected = Pair('[[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]')
    assert str(expected) == str(actual)


# def test_pair_magnitude():
#     a = Pair('[9,1]')
#     b = Pair('[1,9]')
#     c = a + b
#     d = Pair('[[1,2],[[3,4],5]]')
#     e = Pair('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')
#     f = Pair('[[[[1,1],[2,2]],[3,3]],[4,4]]')
#     g = Pair('[[[[3,0],[5,3]],[4,4]],[5,5]]')
#     h = Pair('[[[[5,0],[7,4]],[5,5]],[6,6]]')
#     i = Pair('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]')
#     assert a.magnitue() == 29
#     assert b.magnitue() == 21
#     assert c.magnitue() == 129
#     assert d.magnitue() == 143
#     assert e.magnitue() == 1384
#     assert f.magnitue() == 445
#     assert g.magnitue() == 791
#     assert h.magnitue() == 1137
#     assert i.magnitue() == 3488


# def test_pair_all():
#     pair_strings = [
#         '[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]',
#         '[[[5,[2,8]],4],[5,[[9,9],0]]]',
#         '[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]',
#         '[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]',
#         '[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]',
#         '[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]',
#         '[[[[5,4],[7,7]],8],[[8,3],8]]',
#         '[[9,3],[[9,9],[6,[4,9]]]]',
#         '[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]',
#         '[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]'
#     ]
#     pairs = [Pair(p) for p in pair_strings]
#     actual = sum_pairs(pairs)
#     expected = Pair('[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]')
#     assert str(expected) == str(actual)
#     magnitude = 4140
#     act_mag = actual.magnitue()
#     print(actual)
#     assert magnitude == act_mag
