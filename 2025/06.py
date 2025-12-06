from typing import List
import re
import os
import time

import numpy as np
import itertools


# filename should be name of this .py file with .txt extension
this_filename = os.path.splitext(os.path.basename(__file__))[0] + '.txt'


def read(filename: str, start: int = 1, stop: int = -1, strip: bool = True, 
         splitting_enabled: bool = True, delimiters: List = [' ']):
    """
    Parse txt file into a 2D jagged array of words for each line.\n
    OPTIONAL: Specify start and end line numbers (inclusive), using 1-indexed line numbering. (default: all lines)\n
    OPTIONAL: Pass raw lines with no splitting if needed. (default: split enabled)\n
    OPTIONAL: Use a given list of delimiters for splitting. (default: space)\n
    """
    contents = []

    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(os.path.join(dir_path, filename), 'r') as f:
        if strip:
            lines = [line.strip() for line in f.readlines()]
        else:
            lines = f.readlines()
            for i in range(len(lines)):
                lines[i] = lines[i].rstrip('\n')

    if stop < 1:
        stop = len(lines)
    lines = lines[start-1:stop]

    if splitting_enabled:
        for line in lines:
            contents.append([word for word in re.split('|'.join(map(re.escape, delimiters)), line) if word])
    else:
        contents = lines

    return contents


def part1():
    """
    TODO: part 1 solution
    """
    contents = read(this_filename, start=1, stop=-1, strip=True, 
                    splitting_enabled=True, delimiters=[' ']) # CHANGE AS NEEDED

    height = len(contents) - 1
    width = len(contents[0])

    for h in range(height):
        for w in range(width):
            contents[h][w] = int(contents[h][w])

    mult = [sign == '*' for sign in contents[-1]]
    sum = 0
    for w in range(width):
        if mult[w]:
            result = 1
            for h in range(height):
                result *= contents[h][w]
        else:
            result = 0
            for h in range(height):
                result += contents[h][w]
        sum += result

    return sum


def part2():
    """
    TODO: part 2 solution
    """
    contents = read(this_filename, start=1, stop=-1, strip=False, 
                    splitting_enabled=True, delimiters=['']) # CHANGE AS NEEDED

    height = len(contents) - 1
    width = len(contents[0])
    bottom_row = contents[-1]

    col_low = 0
    col_high = 1

    # look for width of column first
    sum = 0
    while col_low < width:
        mult = bottom_row[col_low] == '*'
        while col_high < width and bottom_row[col_high] not in {'*', '+'}:
            col_high += 1
        if col_high != width:
            col_high -= 1

        nums = []
        for w in range(col_low, col_high):
            curr_num = ''
            for h in range(height):
                if contents[h][w].isnumeric():
                    curr_num += contents[h][w]
            nums.append(int(curr_num))
        
        if mult:
            result = 1
            for num in nums:
                result *= num
        else:
            result = 0
            for num in nums:
                result += num

        sum += result

        col_low = col_high + 1
        col_high += 2

    return sum


def main():
    print("\nPart 1:")
    start_time = time.perf_counter()
    result1 = part1()
    end_time = time.perf_counter()
    print(result1)
    print(f"Runtime: {(end_time - start_time)*1000:.3f} ms")
    
    print("\nPart 2:")
    start_time = time.perf_counter()
    result2 = part2()
    end_time = time.perf_counter()
    print(result2)
    print(f"Runtime: {(end_time - start_time)*1000:.3f} ms")


if __name__ == "__main__":
    main()