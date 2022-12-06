from typing import List, Union, Tuple
import re


this_filename = 'template.txt'


def read(filename: str, delimiters: List[str] = [' '], range: Union[int, Tuple[int, int]] = 0, splitting_enabled: bool = True):
    """
    Parse txt file into a 2D jagged array of words for each line.\n
    Use a given list of delimiters (default: space).\n
    Specify range of line numbers if needed, using 1-indexed line numbering.\n
    For single values, positive range means [0:range] and negative range means [range:len(lines)] (default: all lines).\n
    Pass raw lines with no splitting if needed. (default: split enabled)
    """
    contents = []

    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

        if type(range) is int:
            if range > 0:
                lines = lines[:range-1]
            if range < 0:
                lines = lines[-range-1:]
        else:
            lines = lines[range[0]-1:range[1]-1]

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
    contents = read(this_filename, delimiters=[' '], range=0, splitting_enabled=True) # CHANGE AS NEEDED
    part1_ans = part1(contents)
    part2_ans = part2(contents)
    print(part1_ans)
    print(part2_ans)
    

if __name__ == "__main__":
    main()