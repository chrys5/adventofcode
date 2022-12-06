from typing import List
import re


this_filename = '6.txt'


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
    sum = 0
    for line in contents:
        string = line[0]
        for i in range(3, len(string)):
            set1 = set()
            for j in range(i-3, i+1):
                if string[j] in set1:
                    break
                set1.add(string[j])
            if len(set1) == 4:
                sum += i + 1
                break
    return sum


def part2(contents: List[str]):
    """
    TODO: part 2 solution
    """
    sum = 0
    for line in contents:
        string = line[0]
        for i in range(13, len(string)):
            set1 = set()
            for j in range(i-13, i+1):
                if string[j] in set1:
                    break
                set1.add(string[j])
            if len(set1) == 14:
                sum += i + 1
                break
    return sum


def main():
    contents = parse(this_filename) # CHANGE AS NEEDED
    part1_ans = part1(contents)
    part2_ans = part2(contents)
    print(part1_ans)
    print(part2_ans)


if __name__ == "__main__":
    main()