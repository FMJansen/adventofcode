import re

with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

def get_answer(games):
    possible_games = []

    for line in games:
        game_id = re.findall(r"Game (?P<id>[0-9]+)", line)[0]
        impossible = re.findall(r"(?=(Game (?P<id>[0-9]+).*((\d[5-9]|[2-9]\d{3,}) blue| (\d[4-9]|[2-9]\d{3,}) green| (\d[3-9]|[2-9]\d{3,}) red)))", line)
        if len(impossible) == 0:
            possible_games.append(int(game_id))

    print(sum(possible_games))

get_answer(lines)


def get_powers(games):
    game_powers = []
    for line in games:
        cube_amounts = re.finditer(r"(?=((?P<blue>\d+) blue| (?P<green>\d+) green| (?P<red>\d+) red))", line)
        minimum_amounts = {'red': 0, 'blue': 0, 'green': 0}
        for amount in cube_amounts:
            for color, value in minimum_amounts.items():
                if amount.group(color):
                    if int(amount.group(color)) > int(value):
                        minimum_amounts[color] = amount.group(color)
        game_powers.append(int(minimum_amounts['red']) * int(minimum_amounts['green']) * int(minimum_amounts['blue']))
    
    print(sum(game_powers))

get_powers(lines)