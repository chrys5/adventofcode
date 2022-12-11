from typing import List
import re
import os


this_filename = '10.txt'


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
    global x_during
    x = 1
    x_during = [1]
    for cmd in contents:
        x_during.append(x)
        if cmd[0] == 'addx':
            x_during.append(x)
            x += int(cmd[1])
    
    sum = 0
    for cycle in range(20, 221, 40):
        sum += cycle * x_during[cycle]
    return sum


def part2(contents: List[str]):
    """
    TODO: part 2 solution
    """
    h, w = (6, 40)
    CRT_grid = [[' ' for j in range(w)] for i in range(h)]

    for cycle in range(1, 241):
        i = (cycle - 1) // w
        j = (cycle - 1) % w
        if abs(x_during[cycle] - j) <= 1:
            CRT_grid[i][j] = '#'


    render = '\n'.join([' '.join(line) for line in CRT_grid])
    
    return render

    '''
    my output:
    # # # #   # # # #   # # # #     # #     #     #       # #     # #     # # #
    #               #   #         #     #   #     #         #   #     #   #     #
    # # #         #     # # #     #         # # # #         #   #     #   # # #
    #           #       #         #         #     #         #   # # # #   #     #
    #         #         #         #     #   #     #   #     #   #     #   #     #
    # # # #   # # # #   #           # #     #     #     # #     #     #   # # #
    '''

def main():
    contents = read(this_filename, start=1, stop=-1, splitting_enabled=True, delimiters=[' ']) # CHANGE AS NEEDED
    part1_ans = part1(contents)
    part2_ans = part2(contents)
    print(part1_ans)
    print(part2_ans)


if __name__ == "__main__":
    main()