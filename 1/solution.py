import re

with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

written_numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def parse_number(number):
    try:
        return written_numbers[number]
    except KeyError:
        return number

def get_answer(codes, reg):
    line_codes = []

    for line in codes:
        numbers = re.findall(reg, line)
        first_number = parse_number(numbers[0])
        last_number = parse_number(numbers[-1])
        line_codes.append(int("{0}{1}".format(first_number, last_number)))

    print(sum(line_codes))

get_answer(lines, r"([0-9])")
get_answer(lines, r"(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))")
