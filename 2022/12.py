from typing import List
import re
import os
import string
from collections import deque
import copy


this_filename = '12.txt'


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
    global elev_map, h, w, end_pos, min_path, min_path_len, DIR

    DIR = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    alphabet = string.ascii_lowercase
    heights = dict()
    for i in range(len(alphabet)):
        heights[alphabet[i]] = i
    heights['S'] = -1
    heights['E'] = 26
    
    elev_map = [[heights[char] for char in line[0]] for line in contents]
    h, w = (len(elev_map), len(elev_map[0]))

    start_pos = None
    end_pos = None
    for i in range(h):
        for j in range(w):
            if elev_map[i][j] == -1:
                elev_map[i][j] == 0
                start_pos = (i, j)
            if elev_map[i][j] == 26:
                elev_map[i][j] == 25
                end_pos = (i, j)

    '''
    TODO: implement dijkstra's
    '''
    min_path = []
    min_path_len = h * w
    visited = [[False for j in range(w)] for i in range(h)]
    dfs(deque([start_pos]), visited)

    # orig_map = [[char for char in line[0]] for line in contents] #visualize path
    # path_map = copy.deepcopy(orig_map)
    # for (y, x) in min_path:
    #     path_map[y][x] = '#'
    # orig_render = '\n'.join([''.join(line) for line in orig_map])
    # path_render = '\n'.join([''.join(line) for line in path_map])
    # print(orig_render)
    # print('')
    # print(path_render)

    return min_path_len - 1

def dfs(path, visited):
    global min_path, min_path_len
    y, x = path[-1]
    if x < 0 or x >= w or y < 0 or y >= h or visited[y][x]:
        return
    if len(path) > 1:
        prev_y, prev_x = path[-2]
        if elev_map[y][x] - elev_map[prev_y][prev_x] > 1:
            return

    if (y, x) == end_pos:
        if len(path) < min_path_len:
            min_path = list(path)
            min_path_len = len(path)
            print(min_path_len)
        return
    
    visited[y][x] = True
    DIR.sort(key=lambda d: abs(end_pos[0] - y+d[0]) + abs(end_pos[1] - x+d[1])) #sort directions based on end point
    for dy, dx in DIR:
        path.append((y+dy, x+dx))
        dfs(path, visited)
        path.pop()
    visited[y][x] = False


def part2(contents: List[str]):
    """
    TODO: part 2 solution
    """

    return None


def main():
    contents = read(this_filename, start=1, stop=-1, splitting_enabled=True, delimiters=[' ']) # CHANGE AS NEEDED
    
    print("Part 1:")
    print(part1(contents))
    print("\nPart 2:")
    print(part2(contents))


if __name__ == "__main__":
    main()