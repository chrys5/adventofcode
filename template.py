from typing import List
import re


this_filename = 'template.txt'


def read(filename: str, start: int = 1, stop: int = -1, splitting_enabled: bool = True, delimiters: List[str] = [' ']):
    """
    Parse txt file into a 2D jagged array of words for each line.\n
    Use a given list of delimiters (default: space).\n
    Specify start and end line numbers (inclusive), using 1-indexed line numbering. (default: all lines).\n
    Pass raw lines with no splitting if needed. (default: split enabled)
    """
    contents = []

    with open(filename, 'r') as f:
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

    return None


def part2(contents: List[str]):
    """
    TODO: part 2 solution
    """

    return None


def main():
    contents = read(this_filename, start=1, stop=-1, splitting_enabled=False, delimiters=[' ']) # CHANGE AS NEEDED
    part1_ans = part1(contents)
    part2_ans = part2(contents)
    print(part1_ans)
    print(part2_ans)
    print(contents)
    print(len(contents))

if __name__ == "__main__":
    main()