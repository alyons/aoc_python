from AoC2021.util import parse_file
from AoC2021.day_16 import hex_to_binary_str, parse_packet, process_packet, sum_packet_versions

data = parse_file('./tests/data/day_16.txt')


def test_hex_to_binary_str():
    expected = '110100101111111000101000'
    actual = hex_to_binary_str(data[0])
    assert expected == actual


def test_parse_binary_message_0():
    binary = hex_to_binary_str(data[0])
    packet, index = parse_packet(binary)
    expected = {
        'version': 6,
        'type': 4,
        'value': 2021
    }
    assert packet == expected


def test_parse_binary_message_1():
    binary = hex_to_binary_str(data[1])
    packet, index = parse_packet(binary)
    expected = {
        'version': 1,
        'type': 6,
        'subpackets': [
            {
                'version': 6,
                'type': 4,
                'value': 10
            },
            {
                'version': 2,
                'type': 4,
                'value': 20
            }
        ]
    }
    assert packet == expected


def test_parse_binary_message_2():
    binary = hex_to_binary_str(data[2])
    packet, index = parse_packet(binary)
    expected = {
        'version': 7,
        'type': 3,
        'subpackets': [
            {
                'version': 2,
                'type': 4,
                'value': 1
            },
            {
                'version': 4,
                'type': 4,
                'value': 2
            },
            {
                'version': 1,
                'type': 4,
                'value': 3
            }
        ]
    }
    assert packet == expected


def test_sum_packet_versions_3():
    binary = hex_to_binary_str(data[3])
    packet, index = parse_packet(binary)
    expected = 16
    actual = sum_packet_versions(packet)
    assert expected == actual


def test_sum_packet_versions_4():
    binary = hex_to_binary_str(data[4])
    packet, index = parse_packet(binary)
    expected = 12
    actual = sum_packet_versions(packet)
    assert expected == actual


def test_sum_packet_versions_5():
    binary = hex_to_binary_str(data[5])
    packet, index = parse_packet(binary)
    expected = 23
    actual = sum_packet_versions(packet)
    assert expected == actual


def test_sum_packet_versions_6():
    binary = hex_to_binary_str(data[6])
    packet, index = parse_packet(binary)
    expected = 31
    actual = sum_packet_versions(packet)
    assert expected == actual


def test_process_packet_0():
    binary = hex_to_binary_str(data[0])
    packet, index = parse_packet(binary)
    expected = 2021
    actual = process_packet(packet)
    assert expected == actual


def test_process_packet_full():
    expected_sum = 3
    actual_sum = process_packet(parse_packet(hex_to_binary_str('C200B40A82'))[0])
    assert expected_sum == actual_sum
    expected_product = 54
    actual_product = process_packet(parse_packet(hex_to_binary_str('04005AC33890'))[0])
    assert expected_product == actual_product
    expected_min = 7
    actual_min = process_packet(parse_packet(hex_to_binary_str('880086C3E88112'))[0])
    assert expected_min == actual_min
    expected_max = 9
    actual_max = process_packet(parse_packet(hex_to_binary_str('CE00C43D881120'))[0])
    assert expected_max == actual_max
    expected_g = 1
    actual_g = process_packet(parse_packet(hex_to_binary_str('D8005AC2A8F0'))[0])
    assert expected_g == actual_g
    expected_l = 0
    actual_l = process_packet(parse_packet(hex_to_binary_str('F600BC2D8F'))[0])
    assert expected_l == actual_l
    expected_e = 0
    actual_e = process_packet(parse_packet(hex_to_binary_str('9C005AC2F8F0'))[0])
    assert expected_e == actual_e
    expected = 1
    actual = process_packet(parse_packet(hex_to_binary_str('9C0141080250320F1802104A08'))[0])
    assert expected == actual
