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
    contents = contents[0][0]
    split_contents = contents.split(',')
    parsed_contents = []
    for i in range(len(split_contents)):
        range_split = split_contents[i].split('-')
        parsed_contents.append([range_split[0], range_split[1]])

    ranges_to_append = []
    for i in range(len(parsed_contents)):
        start, end = parsed_contents[i]
        if len(start) < len(end):
            parsed_contents[i][1] = '9' * len(start)
            ranges_to_append.append(['1' + '0' * (len(end) - 1), end])
    
    parsed_contents.extend(ranges_to_append)

    # print(parsed_contents)

    return parsed_contents


def part1(contents: List):
    """
    TODO: part 1 solution
    """

    invalids = 0
    for start, end in contents:
        num_digits = len(start)
        if num_digits % 2 != 0:
            continue
        
        seq = start[:num_digits//2]
        start_int = int(start)
        end_int = int(end)
        while True:
            candidate = int(seq * 2)
            if candidate < start_int:
                seq = str(int(seq) + 1)
                continue
            if candidate > end_int:
                break
            invalids += candidate
            seq = str(int(seq) + 1)

    return invalids


def part2(contents: List):
    """
    TODO: part 2 solution
    """
    # print(contents)

    invalids = 0
    for start, end in contents:
        num_digits = len(start)
        seq_lengths = []
        for i in range(1, (num_digits // 2) + 1):
            if num_digits % i == 0:
                seq_lengths.append((i, num_digits // i))
        
        start_int = int(start)
        end_int = int(end)
        added = set()
        for seq_len, repeats in seq_lengths:
            seq = start[:seq_len]
            while True:
                candidate = int(seq * repeats)
                if candidate < start_int:
                    seq = str(int(seq) + 1)
                    continue
                if candidate > end_int:
                    break
                if not candidate in added:
                    added.add(candidate)
                    # print(f"Adding invalid: {candidate}")
                    invalids += candidate
                seq = str(int(seq) + 1)

    return invalids


def main():
    print("\nParsing/preprocessing input...")
    start_time = time.perf_counter()
    contents = read(this_filename, start=1, stop=-1, splitting_enabled=True, delimiters=[' ']) # CHANGE AS NEEDED
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