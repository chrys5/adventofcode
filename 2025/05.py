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
    ranges = []
    aval = []
    for row in contents:
        if '-' in row:
            ranges.append(tuple(int(n) for n in row.split('-')))
        elif len(row) > 0:
            aval.append(int(row))

    return sorted(ranges), aval


def part1(ranges, aval):
    """
    TODO: part 1 solution
    """

    total = 0
    for n in aval:
        for low, high in ranges:
            if low <= n <= high:
                total += 1
                break
    return total


def part2(ranges):
    """
    TODO: part 2 solution
    """

    total_fresh = 0
    prev_high = -999999
    for low, high in ranges:
        overlap = max(0, prev_high + 1 - low)
        prev_high = max(prev_high, high)
        total_fresh += max(0, high + 1 - low - overlap)
    return total_fresh


def main():
    print("\nParsing/preprocessing input...")
    start_time = time.perf_counter()
    ranges, aval = read(this_filename, start=1, stop=-1, splitting_enabled=False, delimiters=[' ']) # CHANGE AS NEEDED
    end_time = time.perf_counter()
    print(f"Runtime: {(end_time - start_time)*1000:.3f} ms")
    
    print("\nPart 1:")
    start_time = time.perf_counter()
    result1 = part1(ranges, aval)
    end_time = time.perf_counter()
    print(result1)
    print(f"Runtime: {(end_time - start_time)*1000:.3f} ms")
    
    print("\nPart 2:")
    start_time = time.perf_counter()
    result2 = part2(ranges)
    end_time = time.perf_counter()
    print(result2)
    print(f"Runtime: {(end_time - start_time)*1000:.3f} ms")


if __name__ == "__main__":
    main()