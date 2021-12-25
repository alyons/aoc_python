from AoC2021.day_20 import enhance_image, enhance_pixel, find_index, print_image
from AoC2021.util import parse_image

algorithm, image = parse_image('./tests/data/day_20.txt')

def test_find_index():
    key = (2,2)
    expected = 34
    actual = find_index(key, image)
    assert actual == expected


def test_enhance_pixel():
    key = (2,2)
    expected = '#'
    actual = enhance_pixel(key, image, algorithm)
    assert actual == expected


def test_enhance_image_twice():
    test_image = image.copy()
    enhance_image(algorithm, test_image)
    enhance_image(algorithm, test_image)

    print_image(test_image)

    assert 35 == sum(p == '#' for p in test_image.values())
