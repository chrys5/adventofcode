from typing import List
import re
import os
import time

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

    return None


def part2(contents: List):
    """
    TODO: part 2 solution
    """

    return None


def main():
    contents = read(this_filename, start=1, stop=-1, splitting_enabled=True, delimiters=[' ']) # CHANGE AS NEEDED
    
    print("Part 1:")
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