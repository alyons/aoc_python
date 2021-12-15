from AoC2021.util import parse_polymer_formula
from AoC2021.day_14 import apply_polymer_formula_cached

template, rules, elements = parse_polymer_formula('./tests/data/day_14.txt')


def test_apply_polymer_formula_cached():
    expected_10 = { 'N': 865, 'B': 1749, 'C': 298, 'H': 161 }
    actual_10 = apply_polymer_formula_cached(template, rules, 10)
    assert expected_10 == actual_10
    expected_value = 2188189693529
    expected_B = 2192039569602
    expected_H = 3849876073
    actual_40 = apply_polymer_formula_cached(template, rules, 40)
    assert expected_B == actual_40['B']
    assert expected_H == actual_40['H']
    assert expected_value == actual_40['B'] - actual_40['H']
