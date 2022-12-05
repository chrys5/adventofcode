from typing import List
import re


this_filename = 'template.txt'


def parse(filename: str, delimiters: List[str] = [' ']):
    """
    parse txt file into a 2D jagged array of words for each line, using a given list of delimiters (default: space) \n
    only works for ascii characters i think
    """
    contents = []
    with open(filename, 'r') as f:
        for line in [line.strip() for line in f.readlines()]:
            contents.append([word for word in re.split('|'.join(map(re.escape, delimiters)), line) if len(word) > 0])
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
    contents = parse(this_filename) # CHANGE AS NEEDED
    part1_ans = part1(contents)
    part2_ans = part2(contents)
    print(part1_ans)
    print(part2_ans)


if __name__ == "__main__":
    main()