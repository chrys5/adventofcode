from typing import List
import re
import os

import numpy as np
import string
import itertools


this_filename = '8.txt'


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
    contents = np.array(contents)
    locations = {}
    for i in (string.ascii_letters + string.digits):
        locations[i] = []
    for i, row in enumerate(contents):
        for j, cell in enumerate(row):
            if cell != '.':
                locations[cell].append((i, j))
    
    antinodes = set()
    for char in locations:
        for l1, l2 in itertools.combinations(locations[char], 2):
            di = l2[0]-l1[0]
            dj = l2[1]-l1[1]

            a1i = l2[0] + di
            a1j = l2[1] + dj
            a2i = l1[0] - di
            a2j = l1[1] - dj

            antinodes.update([(a1i, a1j), (a2i, a2j)])

    cell_range = set(itertools.product(range(0, len(contents)), range(0, len(contents[0]))))
    antinodes_in_range = cell_range & antinodes

    content_marked = contents.copy()
    for i, j in antinodes_in_range:
        content_marked[i][j] = '#'

    return len(antinodes_in_range)

def part2(contents: List[str]):
    """
    TODO: part 2 solution
    """
    contents = np.array(contents)
    locations = {}
    for i in (string.ascii_letters + string.digits):
        locations[i] = []
    for i, row in enumerate(contents):
        for j, cell in enumerate(row):
            if cell != '.':
                locations[cell].append((i, j))
    
    antinodes = set()
    for char in locations:
        for l1, l2 in itertools.combinations(locations[char], 2):
            di = l2[0]-l1[0]
            dj = l2[1]-l1[1]

            ai, aj = l1[0], l1[1]
            while ai >= 0 and aj >= 0:
                antinodes.add((ai, aj))
                ai -= di
                aj -= dj
            
            ai, aj = l2[0], l2[1]
            while ai < len(contents) and aj < len(contents[0]):
                antinodes.add((ai, aj))
                ai += di
                aj += dj

    cell_range = set(itertools.product(range(0, len(contents)), range(0, len(contents[0]))))
    antinodes_in_range = cell_range & antinodes

    content_marked = contents.copy()
    for i, j in antinodes_in_range:
        content_marked[i][j] = '#'
        
    return len(antinodes_in_range)


def main():
    contents = read(this_filename, start=1, stop=-1, splitting_enabled=True, delimiters=['']) # CHANGE AS NEEDED
    
    print("Part 1:")
    print(part1(contents))
    print("\nPart 2:")
    print(part2(contents))


if __name__ == "__main__":
    main()