from typing import List
import re
import os
import numpy as np

this_filename = '4.txt'


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
    len_contents = len(contents)
    len_contents0 = len(contents[0])

    #pad contents
    contents = np.pad(np.array(contents), 3, mode='constant', constant_values='0')

    sum = 0
    for i in range(3,len_contents+3):
        for j in range(3,len_contents0+3):
            if contents[i][j] != 'X':
                continue

            DIRS = [[(0, 1), (0, 2), (0, 3)],
                    [(0, -1), (0, -2), (0, -3)],
                    [(1, 0), (2, 0), (3, 0)],
                    [(-1, 0), (-2, 0), (-3, 0)],
                    [(1, 1), (2, 2), (3, 3)],
                    [(1, -1), (2, -2), (3, -3)],
                    [(-1, -1), (-2, -2), (-3, -3)],
                    [(-1, 1), (-2, 2), (-3, 3)]]
            for dir in DIRS:
                if contents[i+dir[0][0]][j+dir[0][1]] != 'M':
                    continue
                if contents[i+dir[1][0]][j+dir[1][1]] != 'A':
                    continue
                if contents[i+dir[2][0]][j+dir[2][1]] != 'S':
                    continue
                sum += 1
    return sum


def part2(contents: List[str]):
    """
    TODO: part 2 solution
    """
    len_contents = len(contents)
    len_contents0 = len(contents[0])

    #pad contents
    contents = np.pad(np.array(contents), 1, mode='constant', constant_values='0')

    sum = 0
    for i in range(1,len_contents+1):
        for j in range(1,len_contents0+1):
            if contents[i][j] != 'A':
                continue

            topL = contents[i-1][j+1]
            topR = contents[i+1][j+1]
            botL = contents[i-1][j-1]
            botR = contents[i+1][j-1]

            if not (topL == 'M' and botR == 'S' or topL == 'S' and botR == 'M'):
                continue
            if not (topR == 'M' and botL == 'S' or topR == 'S' and botL == 'M'):
                continue

            sum += 1
            
    return sum


def main():
    contents = read(this_filename, start=1, stop=-1, splitting_enabled=True, delimiters=['']) # CHANGE AS NEEDED
    
    print("Part 1:")
    print(part1(contents))
    print("\nPart 2:")
    print(part2(contents))


if __name__ == "__main__":
    main()