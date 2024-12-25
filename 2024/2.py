from typing import List
import re
import os
import numpy as np

this_filename = '2.txt'


def read(filename: str, start: int = 1, stop: int = -1, splitting_enabled: bool = True, delimiters: List[str] = [' ']):
    """
    Parse txt file into a 2D jagged array of words for each line.\n
    OPTIONAL: Specify start and end line numbers (inclusive), using 1-indexed line numbering. (default: all lines)\n
    OPTIONAL: Pass raw lines with no splitting if needed. (default: split enabled)\n
    OPTIONAL: Use a given list of delimiters for splitting. (default: space)\n
    """
    contents = []

    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(os.path.join(dir_path, filename), 'r') as f:
        lines = [line.strip() for line in f.readlines()]

        if stop < 1:
            stop = len(lines)
        lines = lines[start-1:stop]

        if splitting_enabled:
            for line in lines:
                contents.append([word for word in re.split('|'.join(map(re.escape, delimiters)), line) if len(word) > 0])
        else:
            contents = lines

    return contents


def part1(contents: List[str]):
    """
    TODO: part 1 solution
    """
    safe = 0
    for line in contents:
        line_int = np.array([int(x) for x in line])
        is_sorted_ascending = np.all(line_int[:-1] <= line_int[1:])
        is_sorted_descending = np.all(line_int[:-1] >= line_int[1:])
        if is_sorted_ascending and np.all(line_int[:-1] - line_int[1:] >= -3) and np.all(line_int[:-1] - line_int[1:] <= -1):
            safe += 1
        elif is_sorted_descending and np.all(line_int[:-1] - line_int[1:] <= 3) and np.all(line_int[:-1] - line_int[1:] >= 1):
            safe += 1
    return safe


def part2(contents: List[str]):
    """
    TODO: part 2 solution
    """
    safe = 0
    for line in contents:
        line_int = np.array([int(x) for x in line])
        is_sorted_ascending = np.all(line_int[:-1] <= line_int[1:])
        is_sorted_descending = np.all(line_int[:-1] >= line_int[1:])
        if is_sorted_ascending and np.all(line_int[:-1] - line_int[1:] >= -3) and np.all(line_int[:-1] - line_int[1:] <= -1):
            safe += 1
        elif is_sorted_descending and np.all(line_int[:-1] - line_int[1:] <= 3) and np.all(line_int[:-1] - line_int[1:] >= 1):
            safe += 1
        else:
            for i in range(len(line_int)):
                line_int_minus_i = np.delete(line_int, i)
                is_sorted_ascending = np.all(line_int_minus_i[:-1] <= line_int_minus_i[1:])
                is_sorted_descending = np.all(line_int_minus_i[:-1] >= line_int_minus_i[1:])
                if is_sorted_ascending and np.all(line_int_minus_i[:-1] - line_int_minus_i[1:] >= -3) and np.all(line_int_minus_i[:-1] - line_int_minus_i[1:] <= -1):
                    safe += 1
                    break
                elif is_sorted_descending and np.all(line_int_minus_i[:-1] - line_int_minus_i[1:] <= 3) and np.all(line_int_minus_i[:-1] - line_int_minus_i[1:] >= 1):
                    safe += 1
                    break
    return safe


def main():
    contents = read(this_filename, start=1, stop=-1, splitting_enabled=True, delimiters=[' ']) # CHANGE AS NEEDED
    
    print("Part 1:")
    print(part1(contents))
    print("\nPart 2:")
    print(part2(contents))


if __name__ == "__main__":
    main()