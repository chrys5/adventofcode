from typing import List
import re
import os
import numpy as np
import itertools

this_filename = '3.txt'


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
    flattened_array = list(itertools.chain.from_iterable(contents))
    contents = "".join(flattened_array)

    regex_pattern = r"mul\(([\d]+),([\d]+)\)"
    matches = re.findall(regex_pattern, contents)
    sum = 0
    for i in range(len(matches)):
        sum += int(matches[i][0]) * int(matches[i][1])
    return sum


def part2(contents: List[str]):
    """
    TODO: part 2 solution
    """

    flattened_array = list(itertools.chain.from_iterable(contents))
    contents = "".join(flattened_array)
    do_regex = r"do\(\)"
    dont_regex = r"don't\(\)"
    regex_pattern = r"mul\(([\d]+),([\d]+)\)"
    do_idcs = np.array([match.end() for match in re.finditer(do_regex, contents)])
    dont_idcs = np.array([match.end() for match in re.finditer(dont_regex, contents)])
    match_idcs = np.array([match.end() for match in re.finditer(regex_pattern, contents)])
    matches = re.findall(regex_pattern, contents)
    sum = 0
    for i in range(len(matches)):
        less_than_do = do_idcs[do_idcs < match_idcs[i]]
        less_than_dont = dont_idcs[dont_idcs < match_idcs[i]]
        if less_than_dont.size == 0 or less_than_do[-1] > less_than_dont[-1]:
            sum += int(matches[i][0]) * int(matches[i][1])
    
    return sum


def main():
    contents = read(this_filename, start=1, stop=-1) # CHANGE AS NEEDED
    
    print("Part 1:")
    print(part1(contents))
    print("\nPart 2:")
    print(part2(contents))


if __name__ == "__main__":
    main()