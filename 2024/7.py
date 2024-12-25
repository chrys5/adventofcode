from typing import List
import re
import os
import numpy as np
import itertools


import warnings
warnings.filterwarnings("error", category=RuntimeWarning)

this_filename = '7.txt'


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
    ret = 0
    for row in contents:
        result = int(row[0])
        factors = [int(a) for a in row[2:]]
        for operands in itertools.product([False, True], repeat=len(factors)):
            sum = int(row[1])
            for is_add, factor in zip(operands, factors):
                sum = sum+factor if is_add else sum*factor
                if sum > result:
                    break
            if sum == result:
                ret += result
                break

    return ret


def part2(contents: List[str]):
    """
    TODO: part 2 solution
    """
    ret = 0
    for row in contents:
        result = int(row[0])
        factors = [int(a) for a in row[2:]]
        for operands in itertools.product([0, 1, 2], repeat=len(factors)):
            sum = int(row[1])
            for op, factor in zip(operands, factors):
                if op == 0:
                    sum += factor
                elif op == 1:
                    sum *= factor
                else:
                    sum = sum*np.power(10, np.floor(np.log10(factor))+1) + factor
                if sum > result:
                    break
            if sum == result:
                ret += result
                break

    return ret


def main():
    contents = read(this_filename, start=1, stop=-1, splitting_enabled=True, delimiters=[' ', ':']) # CHANGE AS NEEDED
    
    print("Part 1:")
    print(part1(contents))
    print("\nPart 2:")
    print(part2(contents))


if __name__ == "__main__":
    main()