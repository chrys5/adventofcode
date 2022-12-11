from typing import List
import re
import os
import numpy as np


this_filename = '09.txt'


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
    global DIR
    tpos = np.zeros((2))
    hpos = np.zeros((2))
    DIR = {'U': [0, 1], 'L': [-1, 0], 'D': [0, -1], 'R': [1, 0]}
    tail_visited = set([(0, 0)])

    for cmd in contents:
        delta = DIR[cmd[0]]
        steps = int(cmd[1])
        for step in range(steps):
            hpos += delta
            x_diff, y_diff = hpos - tpos
            if x_diff == -2:
                tpos = hpos + DIR['R']
            if x_diff == 2:
                tpos = hpos + DIR['L']
            if y_diff == -2:
                tpos = hpos + DIR['U']
            if y_diff == 2:
                tpos = hpos + DIR['D']
            tail_visited.add((int(tpos[0]), int(tpos[1])))

    return len(tail_visited)


def part2(contents: List[str]):
    """
    TODO: part 2 solution
    """
    knots = np.zeros((10, 2))
    tail_visited = set([(0, 0)])

    for cmd in contents:
        delta = DIR[cmd[0]]
        steps = int(cmd[1])
        for step in range(steps):
            knots[0] += delta
            for i in range(1, 10):
                x_diff, y_diff = knots[i-1] - knots[i]
                if abs(x_diff) == 2 and abs(y_diff) == 2:
                    knots[i] = knots[i-1] - [x_diff / 2, y_diff / 2] #for diagonal edge case
                else :
                    if x_diff == -2:
                        knots[i] = knots[i-1] + DIR['R']
                    if x_diff == 2:
                        knots[i] = knots[i-1] + DIR['L']
                    if y_diff == -2:
                        knots[i] = knots[i-1] + DIR['U']
                    if y_diff == 2:
                        knots[i] = knots[i-1] + DIR['D']
            tail_visited.add((int(knots[9][0]), int(knots[9][1])))

    return len(tail_visited)


def main():
    contents = read(this_filename, start=1, stop=-1, splitting_enabled=True, delimiters=[' ']) # CHANGE AS NEEDED
    part1_ans = part1(contents)
    part2_ans = part2(contents)
    print(part1_ans)
    print(part2_ans)


if __name__ == "__main__":
    main()