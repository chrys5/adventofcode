from typing import List
import re
import os
import numpy as np

this_filename = '5.txt'
this_filename2 = '5_1.txt'


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


def part1(contents):
    """
    TODO: part 1 solution
    """
    orders_raw = np.array(contents[0]).astype(int)
    before = {}
    after = {}
    for pair in orders_raw:
        if not pair[0] in after:
            after[pair[0]] = [pair[1]]
        else:
            after[pair[0]].append(pair[1])
        
        if not pair[1] in before:
            before[pair[1]] = [pair[0]]
        else:
            before[pair[1]].append(pair[0])

    sum = 0
    updates_raw = contents[1]
    for update in updates_raw:
        bad_update = False
        update = np.array(update).astype(int)
        for i, n in enumerate(update):
            if len(np.intersect1d(before[n], update[i+1:])) > 0:
                bad_update = True
                break
        if bad_update:
            continue

        sum += update[len(update)//2]
    return sum


def part2(contents):
    """
    TODO: part 2 solution
    """
    orders_raw = np.array(contents[0]).astype(int)
    before = {}
    after = {}
    for pair in orders_raw:
        if not pair[0] in after:
            after[pair[0]] = [pair[1]]
        else:
            after[pair[0]].append(pair[1])
        
        if not pair[1] in before:
            before[pair[1]] = [pair[0]]
        else:
            before[pair[1]].append(pair[0])

    sum = 0
    updates_raw = contents[1]
    for update in updates_raw:
        bad_update = False
        update = np.array(update).astype(int)
        for i, n in enumerate(update):
            if len(np.intersect1d(before[n], update[i+1:])) > 0:
                bad_update = True
                break
        if not bad_update:
            continue

        update_set = set(update)
        i = 0
        num = 0
        while i < len(update)//2 + 1:
            for n in update_set:
                update_set.remove(n)
                if len(np.intersect1d(before[n], list(update_set))) == 0:
                    i += 1
                    num = n
                    break
                update_set.add(n)

        sum += num
    return sum


def main():
    contents1 = read(this_filename, start=1, stop=-1, splitting_enabled=True, delimiters=['|']) # CHANGE AS NEEDED
    contents2 = read(this_filename2, splitting_enabled=True, delimiters=[','])
    
    print("Part 1:")
    print(part1((contents1, contents2)))
    print("\nPart 2:")
    print(part2((contents1, contents2)))


if __name__ == "__main__":
    main()