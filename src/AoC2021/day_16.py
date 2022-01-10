from typing import Dict, List, Tuple
from math import prod


def hex_to_binary_char(hex: str) -> str:
    match hex:
        case '0': return '0000'
        case '1': return '0001'
        case '2': return '0010'
        case '3': return '0011'
        case '4': return '0100'
        case '5': return '0101'
        case '6': return '0110'
        case '7': return '0111'
        case '8': return '1000'
        case '9': return '1001'
        case 'A': return '1010'
        case 'B': return '1011'
        case 'C': return '1100'
        case 'D': return '1101'
        case 'E': return '1110'
        case 'F': return '1111'


def hex_to_binary_str(hex: str) -> str:
    chunks = [hex_to_binary_char(h) for h in hex]
    return ''.join(chunks)


def parse_literal_value(binary: str, index: int) -> tuple[int, int]:
    _literal = ''
    _l = '1'
    while _l[0] == '1':
        _l = binary[index:index + 5]
        _literal += _l[1:5]                 
        index += 5

    return (int(_literal, 2), index)


def parse_packet(binary: str, index: int = 0) -> Tuple[Dict, int]:
    packet = {}

    _v = binary[index:index + 3]
    index += 3
    packet['version'] = int(_v, 2)
    _t = binary[index:index + 3]
    index += 3
    packet['type'] = int(_t, 2)

    match packet['type']:
        case 4: # Literal Value
            value, index = parse_literal_value(binary, index)
            packet['value'] = value
        case x if x != 4:
            _i = binary[index:index + 1]
            index += 1
            # print(f'Len Type: {_i}')
            _len = binary[index:index + 15] if _i == '0' else binary[index: index + 11]
            # print(f'Len String: {_len}')
            index += 15 if _i == '0' else 11
            subpacket_length = int(_len, 2)
            # print(f'Subpacket Length: {subpacket_length}')
            if _i == '0': # Process by number of bits
                end_index = index + subpacket_length
                subpackets = []
                while index < end_index:
                    subpacket, index = parse_packet(binary, index)
                    subpackets.append(subpacket.copy())
                packet['subpackets'] = subpackets
            if _i == '1': # Process by number of subpackets
                subpackets = []
                while len(subpackets) < subpacket_length:
                    subpacket, index = parse_packet(binary, index)
                    subpackets.append(subpacket.copy())
                packet['subpackets'] = subpackets
    
    # remaining_bits = binary[index:]
    # if '1' in remaining_bits: print('There is more processing to do...')

    return (packet, index)


def sum_packet_versions(packet: Dict) -> int:
    version_sum = packet['version']

    if 'subpackets' in packet:
        for p in packet['subpackets']:
            version_sum += sum_packet_versions(p)

    return version_sum


def process_packet(packet: Dict) -> int:
    match packet['type']:
        case 4:
            return packet['value']
        case x if x != 4:
            p_values = [process_packet(p) for p in packet['subpackets']]
            if x == 0:
                return sum(p_values)
            elif x == 1:
                return prod(p_values)
            elif x == 2:
                return min(p_values)
            elif x == 3:
                return max(p_values)
            elif x == 5:
                return int(p_values[0] > p_values[1])
            elif x == 6:
                return int(p_values[0] < p_values[1])
            elif x == 7:
                return int(p_values[0] == p_values[1])
