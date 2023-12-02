
import re

from read_file import read_file


def get_first_and_last_item(items: list) -> list:
    return [translate_word_to_digit(items[0]), translate_word_to_digit(items[-1])]


def join_digits_to_one_string(digits: list) -> str:
    if len(digits) == 1:
        return digits[0]
    if len(digits) > 1:
        return "".join(digits)


def translate_word_to_digit(item: str):
    hash_map = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9' }
    digit = hash_map.get(item)
    if not digit:
        return item
    return digit


def estimate_pattern_positions(data: str) -> list:
    patterns = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '0', '1', '2', '3', '4',
                '5', '6', '7', '8', '9']
    
    patterns_with_position = []
    for pattern in patterns:
        pattern_spans = list(re.finditer(pattern, data))
        pattern_span_sums = list(map(lambda x: sum(x.span()), pattern_spans))
        for number in pattern_span_sums:
            patterns_with_position.append((pattern, number))
    return patterns_with_position


def find_numbers_in_string(data: str) -> list[str]:
    patterns_with_position = estimate_pattern_positions(data)
    sorted_patterns = sorted(patterns_with_position, key=lambda x: x[1])
    numbers: list[str] = [item[0] for item in sorted_patterns]
    return numbers


def recover_calibration_values_from_digits(document_lines: list) -> list:
    searched_pattern = '[0-9]'
    recovered_digits = list(map(lambda item: re.findall(searched_pattern, item), document_lines))
    first_and_last_digit = list(map(lambda item: get_first_and_last_item(item), recovered_digits))
    recovered_numbers = list(map(lambda item: int(join_digits_to_one_string(item)), first_and_last_digit))
    return recovered_numbers


def recover_calibration_values_from_digits_and_words(document_lines: list) -> list:
    recovered_numbers = list(map(lambda item: find_numbers_in_string(item), document_lines))
    first_and_last_digit = list(map(lambda item: get_first_and_last_item(item), recovered_numbers))
    recovered_integers = list(map(lambda item: int(join_digits_to_one_string(item)), first_and_last_digit))
    return recovered_integers


read_lines = read_file('input1.txt')
calibration_values_from_digits = recover_calibration_values_from_digits(read_lines)
print(sum(calibration_values_from_digits))

calibration_values_from_digits_and_words = recover_calibration_values_from_digits_and_words(read_lines)
print(sum(calibration_values_from_digits_and_words))


