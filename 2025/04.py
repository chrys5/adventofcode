from typing import List
import re
import os
import time
import copy

import numpy as np
import itertools
from PIL import Image, ImageDraw


# filename should be name of this .py file with .txt extension
this_filename = os.path.splitext(os.path.basename(__file__))[0] + '.txt'


def read(filename: str, start: int = 1, stop: int = -1, splitting_enabled: bool = True, delimiters: List = [' ']):
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

    # ADDITIONAL PROCESSING HERE IF NEEDED
    for i in range(len(contents)):
        contents[i] = [chr for chr in contents[i]]

    return contents

def part1(contents: List):
    """
    TODO: part 1 solution
    """
    DIR = [
        (0, 1),   # right
        (1, 0),   # down
        (0, -1),  # left
        (-1, 0),  # up
        (1, 1),   # down-right
        (1, -1),  # down-left
        (-1, 1),  # up-right
        (-1, -1)  # up-left
    ]

    accessable_toilet_papers = 0
    accessable_coords = []
    for i, row in enumerate(contents):
        for j, char in enumerate(row):
            if char != '@':
                continue
            adj_toilet_papers = 0
            for d in DIR:
                adj_i = i + d[0]
                adj_j = j + d[1]
                if 0 <= adj_i < len(contents) and 0 <= adj_j < len(row) and contents[adj_i][adj_j] == '@':
                    adj_toilet_papers += 1 
                if adj_toilet_papers >= 4:
                    break
            
            if adj_toilet_papers < 4:
                accessable_toilet_papers += 1
                accessable_coords.append((i, j))
    return accessable_toilet_papers, accessable_coords


def part2(contents: List):
    """
    TODO: part 2 solution
    """

    accessable_toilet_papers_total = 0
    map_over_time = [copy.deepcopy(contents)]
    while True:
        accessable_toilet_papers, accessable_coords = part1(contents)
        accessable_toilet_papers_total += accessable_toilet_papers
        for coord in accessable_coords:
            contents[coord[0]][coord[1]] = '.'
        map_over_time.append(copy.deepcopy(contents))
        if accessable_toilet_papers == 0:
            break

    return accessable_toilet_papers_total, map_over_time


def save_map_animation(map_over_time, filename, scale=8, duration_ms=1000,
                       tp_color=(245, 245, 245), empty_color=(20, 20, 50), on_char='@'):
    
    frames = []
    for grid in map_over_time:
        h = len(grid)
        w = len(grid[0]) if h > 0 else 0
        arr = np.array([[tp_color if grid[i][j] == on_char else empty_color for j in range(w)] for i in range(h)], dtype=np.uint8)

        img = Image.fromarray(arr, mode='RGB')
        if scale != 1:
            img = img.resize((img.width * scale, img.height * scale), resample=Image.NEAREST)

        frames.append(img.convert('P'))

    frames[0].save(
        filename,
        save_all=True,
        append_images=frames[1:],
        duration=duration_ms,
        loop=0,
        optimize=False
    )


def main():
    contents = read(this_filename, start=1, stop=-1, splitting_enabled=False, delimiters=['']) # CHANGE AS NEEDED
    
    print("Part 1:")
    start_time = time.perf_counter()
    result1, _ = part1(contents)
    end_time = time.perf_counter()
    print(result1)
    print(f"Runtime: {(end_time - start_time)*1000:.3f} ms")
    
    print("\nPart 2:")
    start_time = time.perf_counter()
    result2, map_over_time = part2(contents)
    end_time = time.perf_counter()
    print(result2)
    print(f"Runtime: {(end_time - start_time)*1000:.3f} ms")

    save_map_animation(map_over_time, filename='2025_04_map_animation.gif', duration_ms=82)


if __name__ == "__main__":
    main()