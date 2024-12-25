from typing import List
import re
import os

import numpy as np

this_filename = '9.txt'


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
    contents = np.array(contents).astype(int).reshape((len(contents[0]),))
    block_szs = contents[0:len(contents):2]
    free_space = contents[1:len(contents):2]
    disk_space = np.zeros((np.sum(contents),))

    i_begin = 0
    i_end = len(block_szs) - 1
    i_disk = 0
    while True:
        # populate 

    return None


def part2(contents: List[str]):
    """
    TODO: part 2 solution
    """

    return None


def main():
    contents = read(this_filename, start=1, stop=-1, splitting_enabled=True, delimiters=['']) # CHANGE AS NEEDED
    
    print("Part 1:")
    print(part1(contents))
    print("\nPart 2:")
    print(part2(contents))


if __name__ == "__main__":
    main()