import re
from functools import reduce

from read_file import read_file

class Number:
    def __init__(self, value, span, y_position):
        self.span = span
        self.value = value
        self.y_position = y_position
        self.positions = self.calculate_positions_occupancy()

    def calculate_positions_occupancy(self):
        positions = []
        for x_position in range(self.span[0], self.span[1]):
            positions.append((x_position, self.y_position))
        return positions


class Star:
    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position
        self.sensitive_positions = self.calculate_sensitive_positions()

    def calculate_sensitive_positions(self):
        positions = []
        positions.append((self.x_position + 1, self.y_position))
        positions.append((self.x_position + 1, self.y_position + 1))
        positions.append((self.x_position + 1, self.y_position - 1))
        positions.append((self.x_position, self.y_position + 1))
        positions.append((self.x_position, self.y_position - 1))
        positions.append((self.x_position - 1, self.y_position))
        positions.append((self.x_position - 1, self.y_position + 1))
        positions.append((self.x_position - 1, self.y_position - 1))

        return positions


def find_numbers_in_matrix(matrix):
    numbers = []
    for m_value in range(len(matrix)):
        numbers_occurrence_in_row = re.finditer(r'\d+', matrix[m_value])
        numbers_in_row = list(map(lambda x:  Number(int(x.group()), x.span(), m_value), numbers_occurrence_in_row))
        numbers.extend(numbers_in_row)
    return numbers


def find_stars_in_matrix(matrix):
    stars = []
    for m_value in range(len(matrix)):
        stars_occurrence_in_row = re.finditer(r'\*', matrix[m_value])
        stars_in_row = list(map(lambda x:  Star(x.span()[0], m_value), stars_occurrence_in_row))
        stars.extend(stars_in_row)
    return stars


def return_if_2_numbers_close_to_star (stars, numbers):
    gears = []
    for star in stars:
        close_numbers = set()
        for number in numbers:
            for number_position in number.positions:
                if number_position in star.sensitive_positions:
                    close_numbers.add(number.value)
        if len(close_numbers) == 2:
            gears.append(list(close_numbers))
    return gears


def calculate_gear_ratios (gears):
    gear_ratios = []
    for gear in gears:
        gear_ratios.append(reduce(lambda x, y: x * y, gear))
    return gear_ratios


def calculate_matrix_edges(matrix):
    m_value = len(matrix) - 1
    n_value = len(matrix[0]) - 1
    return m_value, n_value


def prepare_matrix(data):
    matrix = list(map(lambda x: "." + x.replace("\n", "."), data))
    m_value, n_value = calculate_matrix_edges(matrix)
    m_row_pattern = "." * n_value
    matrix.insert(0, m_row_pattern)  # Add at the beginning
    matrix.append(m_row_pattern)
    return matrix


data = read_file('input3.txt')
matrix = prepare_matrix(data)
numbers = find_numbers_in_matrix(matrix)
stars = find_stars_in_matrix(matrix)
gears = return_if_2_numbers_close_to_star(stars, numbers)
gear_ratios = calculate_gear_ratios(gears)

print(sum(gear_ratios))

