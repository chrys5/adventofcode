from typing import List
import re
import os
import sys
import time

from utils import read_file

# filename should be absolute path name of this .py file with .txt extension
this_filename = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), 
    os.path.splitext(os.path.basename(__file__))[0] + '.txt')

# -------------------------------------------------------------------------
def part1():
    """
    TODO: part 1 solution
    """
    contents = read_file(this_filename, strip=False, delimiters=[' '], line_range=(None, None)) # CHANGE AS NEEDED

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
    contents = read_file(this_filename, strip=False, delimiters=None, line_range=(None, None)) # CHANGE AS NEEDED

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
# -------------------------------------------------------------------------

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