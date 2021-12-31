from copy import deepcopy
from sys import maxsize


def find_index(key: tuple[int, int], image: dict[tuple[int,int], str], even_enhance: bool) -> int:
    binary = ''
    _x, _y = key

    for _dy in range(-1, 2):
        for _dx in range(-1, 2):
            _k = (_x + _dx, _y + _dy)
            if not _k in image:
                binary += '1' if even_enhance else '0'
            else:
                binary += '0' if image[_k] == '.' else '1'

    return int(binary, 2)


def enhance_pixel(key: tuple[int,int], image: dict[tuple[int,int]], algorithm: str, even_enhance: bool) -> str:
    index = find_index(key, image, even_enhance)
    return algorithm[index]


def enhance_image(algorithm, image, even_enhance: bool = False) -> dict[tuple[int,int]]:
    _new_image = deepcopy(image)

    min_x = min([k[0] for k in image.keys()]) - 1
    min_y = min([k[1] for k in image.keys()]) - 1
    max_x = max([k[0] for k in image.keys()]) + 1
    max_y = max([k[1] for k in image.keys()]) + 1

    even_enhance &= algorithm[0] == '#' and  algorithm[511] == '.'

    for _y in range(min_y, max_y + 1):
        for _x in range(min_x, max_x + 1):
            key = (_x, _y)
            _new_image[key] = enhance_pixel(key, image, algorithm, even_enhance)

    for k in _new_image:
        image[k] = _new_image[k]


def print_image(image: dict[tuple[int,int], str]):
    min_x = min([k[0] for k in image.keys()])
    min_y = min([k[1] for k in image.keys()])
    max_x = max([k[0] for k in image.keys()])
    max_y = max([k[1] for k in image.keys()])

    for _y in range(min_y, max_y + 1):
        _l = ''
        for _x in range(min_x, max_x + 1):
            key = (_x, _y)
            if not key in image:
                _l += '.'
            else:
                _l += image[key]
        print(_l)
