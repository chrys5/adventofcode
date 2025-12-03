from typing import List
import re
import os

import numpy as np
import itertools


# filename should be name of this .py file with .txt extension
this_filename = os.path.splitext(os.path.basename(__file__))[0] + '.txt'


def read(filename: str, start: int = 1, stop: int = -1, splitting_enabled: bool = True, delimiters: List = [' ']):
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

    # ADDITIONAL PROCESSING HERE IF NEEDED
    
    return contents


def part1(contents: List):
    """
    TODO: part 1 solution
    """

    sum = 0
    for line in contents:
        line_max = (line[0], '0')
        monotonic_stack = [line[0]]
        for num in line[1:]:
            line_max = max(line_max, (monotonic_stack[0], num))
            while len(monotonic_stack) > 0 and num > monotonic_stack[-1]:
                monotonic_stack.pop()
            monotonic_stack.append(num)
        sum += int(line_max[0]) * 10 + int(line_max[1])

    return sum


def part2(contents: List):
    """
    TODO: part 2 solution
    """

    LINE_LEN = len(contents[0])
    sum = 0
    for line in contents:
        monotonic_stack = []
        for i, num in enumerate(line):
            while LINE_LEN - i > 12 - len(monotonic_stack) and len(monotonic_stack) > 0 and num > monotonic_stack[-1]:
                monotonic_stack.pop()

            if len(monotonic_stack) < 12:
                monotonic_stack.append(num)

        line_max = int(''.join(monotonic_stack))
        # print(line_max)
        sum += line_max
        
    return sum


def main():
    contents = read(this_filename, start=1, stop=-1, splitting_enabled=False, delimiters=[' ']) # CHANGE AS NEEDED
    
    print("Part 1:")
    print(part1(contents))
    print("\nPart 2:")
    print(part2(contents))


if __name__ == "__main__":
    main()