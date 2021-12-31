from AoC2021.util import parse_image
from AoC2021.day_20 import enhance_image

def main():
    print('Welcome to Day 20')
    
    algorithm, image = parse_image('./data/day_20.txt')

    for i in range(50):
        enhance_image(algorithm, image, i % 2 == 1)
    
    pixels = sum(p == '#' for p in image.values())

    print(f'Lit Pixels: {pixels!r}')


if __name__ == '__main__':
    main()