from typing import List
import re
from collections import deque


this_filename = '2022\\7.txt'


def read(filename: str, start: int = 1, stop: int = -1, splitting_enabled: bool = True, delimiters: List[str] = [' ']):
    """
    Parse txt file into a 2D jagged array of words for each line.\n
    OPTIONAL: Specify start and end line numbers (inclusive), using 1-indexed line numbering. (default: all lines)\n
    OPTIONAL: Pass raw lines with no splitting if needed. (default: split enabled)\n
    OPTIONAL: Use a given list of delimiters for splitting. (default: space)\n
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

class Dir:
    def __init__(self, parent, name):
        self.subdirs = dict()
        self.files = set()
        self.size = 0
        self.parent = parent
        self.name = name

def part1(contents: List[str]):
    """
    TODO: part 1 solution
    """
    global root_dir
    root_dir = Dir(None, '/')
    curr_dir = root_dir
    for line in contents:
        if line[0:2] == ['$', 'cd']:
            match line[2]:
                case '..':
                    curr_dir = curr_dir.parent
                case '/':
                    curr_dir = root_dir
                case new_dir_name:
                    curr_dir = curr_dir.subdirs[new_dir_name]
        elif line[0:2] == ['$', 'ls']:
            continue
        elif line[0] == 'dir':
            new_dir_name = line[1]
            if not new_dir_name in curr_dir.subdirs:
                curr_dir.subdirs[new_dir_name] = Dir(curr_dir, new_dir_name)
        else:
            file_size, file_name = line
            if not file_name in curr_dir.files:
                curr_dir.files.add(line[1])
                dir_up = curr_dir
                while (dir_up != None):
                    dir_up.size += int(file_size)
                    dir_up = dir_up.parent
    
    sum = 0
    queue = deque()
    queue.append(root_dir)
    while queue:
        curr_dir = queue.popleft()
        if curr_dir.size <= 100000:
            sum += curr_dir.size
        queue.extend(curr_dir.subdirs.values())
    return sum


def part2(contents: List[str]):
    sizes = []
    queue = deque()
    queue.append(root_dir)
    while queue:
        curr_dir = queue.popleft()
        sizes.append(curr_dir.size)
        queue.extend(curr_dir.subdirs.values())

    unused_space = 70000000 - root_dir.size
    space_needed = 30000000 - unused_space
    min_size = min(size for size in sizes if size > space_needed)

    return min_size


def main():
    contents = read(this_filename, start=1, stop=-1, splitting_enabled=True, delimiters=[' ']) # CHANGE AS NEEDED
    part1_ans = part1(contents)
    part2_ans = part2(contents)
    print(part1_ans)
    print(part2_ans)


if __name__ == "__main__":
    main()