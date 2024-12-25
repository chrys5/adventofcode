from typing import List
import re
import os
import numpy as np


this_filename = '6.txt'


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
    contents = np.pad(np.array(contents), 1, mode='constant', constant_values='0')
    start_pos = np.where(contents == '^')
    start_pos = list(zip(start_pos[0], start_pos[1]))[0]
    pos_set = set()
    
    i = start_pos[0]
    j = start_pos[1]
    dir = (-1, 0)
    next_dir = {
        (0, 1) : (1, 0),
        (1, 0) : (0, -1),
        (0, -1) : (-1, 0),
        (-1, 0) : (0, 1)
    }
    while contents[i][j] != '0':
        pos_set.add((i, j))
        while contents[i + dir[0]][j + dir[1]] == '#':
            dir = next_dir[dir]
        i += dir[0]
        j += dir[1]
    return len(pos_set)

def part1_2(contents: List[str]):
    """
    TODO: part 1 solution
    """
    contents = np.pad(np.array(contents), 1, mode='constant', constant_values='0')
    start_pos = np.where(contents == '^')
    start_pos = list(zip(start_pos[0], start_pos[1]))[0]
    pos_set = set()
    
    i = start_pos[0]
    j = start_pos[1]
    dir = (-1, 0)
    next_dir = {
        (0, 1) : (1, 0),
        (1, 0) : (0, -1),
        (0, -1) : (-1, 0),
        (-1, 0) : (0, 1)
    }
    while contents[i][j] != '0':
        pos_set.add((i, j))
        while contents[i + dir[0]][j + dir[1]] == '#':
            dir = next_dir[dir]
        i += dir[0]
        j += dir[1]
    return pos_set


def part2(contents: List[str]):
    """
    TODO: part 2 solution
    """
    pos_set_pt1 = part1_2(contents)

    contents = np.pad(np.array(contents), 1, mode='constant', constant_values='0')
    start_pos = np.where(contents == '^')
    start_pos = list(zip(start_pos[0], start_pos[1]))[0]

    obstructions = 0
    for obstruction_pos in pos_set_pt1:
        contents[obstruction_pos[0]][obstruction_pos[1]] = '#'

        pos_set = set()
        i = start_pos[0]
        j = start_pos[1]
        dir = (-1, 0)
        next_dir = {
            (0, 1) : (1, 0),
            (1, 0) : (0, -1),
            (0, -1) : (-1, 0),
            (-1, 0) : (0, 1)
        }
        while contents[i][j] != '0' and not (i, j, dir) in pos_set:
            pos_set.add((i, j, dir))
            while contents[i + dir[0]][j + dir[1]] == '#':
                dir = next_dir[dir]
            i += dir[0]
            j += dir[1]
        
        if contents[i][j] != '0':
            obstructions += 1

        contents[obstruction_pos[0]][obstruction_pos[1]] = '.'
    return obstructions


def main():
    contents = read(this_filename, start=1, stop=-1, splitting_enabled=True, delimiters=['']) # CHANGE AS NEEDED
    
    print("Part 1:")
    print(part1(contents))
    print("\nPart 2:")
    print(part2(contents))


if __name__ == "__main__":
    main()