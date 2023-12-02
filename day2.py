import re

from read_file import read_file

games = read_file('input2.txt')


def find_max_number_for_cube_colour_in_set(cube_color, cube_sets):
    max_cube_number = 0
    searched_pattern = r'\d+\s' + cube_color
    cubes = re.findall(searched_pattern, cube_sets)
    for cube in cubes:
        [cube_number, _] = cube.split()
        max_cube_number = max(max_cube_number, int(cube_number))
    return max_cube_number


def find_max_numbers_for_all_cube_colours_in_game(game):
    game, cube_sets = game.split(":")
    _, game_id = game.split()
    red_cube_max_number, blue_cube_max_number, green_cube_max_number = map(
        lambda color: find_max_number_for_cube_colour_in_set(color, cube_sets), ['red', 'blue', 'green'])

    return {"game": int(game_id), "red_max": red_cube_max_number, "blue_max": blue_cube_max_number,
            "green_max": green_cube_max_number}


def check_if_game_possible(red: int, blue: int, green: int, game: str):
    result = find_max_numbers_for_all_cube_colours_in_game(game)
    return result.get('game') \
        if result.get('red_max') <= red and result.get('blue_max') <= blue and result.get('green_max') <= green \
        else 0


possible_games = list(map(lambda game: check_if_game_possible(12, 14, 13, game), games))
sum_of_possible_game_ids = sum(possible_games)
print(sum_of_possible_game_ids)


def calculate_power_of_cubes_set_in_game(game):
    _, cube_sets = game.split(":")
    red_cube_max_number, blue_cube_max_number, green_cube_max_number = map(
        lambda color: find_max_number_for_cube_colour_in_set(color, cube_sets), ['red', 'blue', 'green'])
    return red_cube_max_number * blue_cube_max_number * green_cube_max_number


cube_sets_power_for_all_games = list(map(lambda game: calculate_power_of_cubes_set_in_game(game), games))
sum_of_powers = sum(cube_sets_power_for_all_games)
print(sum_of_powers)
