from typing import List
import re
import os
import time

import numpy as np
import itertools


this_filename = os.path.splitext(os.path.basename(__file__))[0] + '.txt'


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

    # ADDITIONAL PROCESSING HERE IF NEEDED
    for i in range(len(contents)):
        contents[i] = (contents[i][0], int(contents[i][1:]))

    return contents


def part1(contents: List[tuple]):
    """
    TODO: part 1 solution
    """

    dial = 50
    ret = 0
    for dir, value in contents:
        if dir == 'R':
            dial = (dial + value) % 100
        else:
            dial = (dial - value) % 100
        if dial == 0:
            ret += 1
    return ret


def part2(contents: List[tuple]):
    """
    TODO: part 2 solution
    """

    dial = 50
    ret = 0
    for dir, value in contents:
        new_val = 0
        if dir == 'R':
            new_val = dial + value
        else:
            new_val = dial - value
        
        if new_val <= 0:
            ret += (-new_val // 100)
            if dial != 0:
                ret += 1
        elif new_val >= 100:
            ret += new_val // 100
        
        dial = new_val % 100
        # print(command, value, dial, ret)
    return ret


def main():
    print("\nParsing/preprocessing input...")
    start_time = time.perf_counter()
    contents = read(this_filename, start=1, stop=-1, splitting_enabled=False, delimiters=[' ']) # CHANGE AS NEEDED
    end_time = time.perf_counter()
    print(f"Runtime: {(end_time - start_time)*1000:.3f} ms")
    
    print("\nPart 1:")
    start_time = time.perf_counter()
    result1 = part1(contents)
    end_time = time.perf_counter()
    print(result1)
    print(f"Runtime: {(end_time - start_time)*1000:.3f} ms")
    
    print("\nPart 2:")
    start_time = time.perf_counter()
    result2 = part2(contents)
    end_time = time.perf_counter()
    print(result2)
    print(f"Runtime: {(end_time - start_time)*1000:.3f} ms")


if __name__ == "__main__":
    main()