from AoC2021.day_16 import hex_to_binary_str, parse_packet, process_packet, sum_packet_versions
from AoC2021.util import parse_file

def main():
    print('Welcome to Day 10 of Advent of Code 2021')

    data = parse_file('./data/day_16.txt')
    binary = hex_to_binary_str(data[0])

    packet, index = parse_packet(binary)
    
    version_sum = sum_packet_versions(packet)

    print(f'Version Sum: {version_sum}')

    output = process_packet(packet)

    print(f'Output: {output}')


if __name__ == '__main__':
    main()
