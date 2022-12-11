from typing import List
import re
import os

this_filename = '08.txt'


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
    global grid, h, w, dp
    grid = []
    for line in contents:
        grid.append([int(x) for x in line[0]])
    
    h = len(grid)
    w = len(grid[0])
    dp = [[[0 for k in range(4)] for j in range(w)] for i in range(h)] #0: up, 1: left, 2: down, 3: right
    for i in range(1, h-1):
        for j in range(1, w-1):
            dp[i][j][0] = max(grid[i-1][j], dp[i-1][j][0])
            dp[i][j][1] = max(grid[i][j-1], dp[i][j-1][1])
    
    for i in range(h-2, 0, -1):
        for j in range(w-2, 0, -1):
            dp[i][j][2] = max(grid[i+1][j], dp[i+1][j][2])
            dp[i][j][3] = max(grid[i][j+1], dp[i][j+1][3])
    
    sum = 0
    for i in range(h):
        for j in range(w):
            if i==0 or j==0 or i==h-1 or j==h-1 or grid[i][j] > min(dp[i][j]):
                sum+=1
    
    return sum


def part2(contents: List[str]):
    """
    TODO: part 2 solution
    """
    max_score = 1 #got lazy
    for i in range(0, h):
        for j in range(0, w):
            curr_height = grid[i][j]

            a = i-1
            up = 0
            while (a >= 0 and grid[a][j] < curr_height):
                up+=1
                a-=1
            if a >= 0:
                up+=1
            
            a = j-1
            left = 0
            while (a >= 0 and grid[i][a] < curr_height):
                left+=1
                a-=1
            if a >= 0:
                left+=1

            a = i+1
            down = 0
            while (a < h and grid[a][j] < curr_height):
                down+=1
                a+=1
            if a < h:
                down+=1
            
            a = j+1
            right = 0
            while (a < w and grid[i][a] < curr_height):
                right+=1
                a+=1
            if a < w:
                right+=1

            max_score = max(max_score, up*left*down*right)

    return max_score


def main():
    contents = read(this_filename, start=1, stop=-1, splitting_enabled=True, delimiters=[' ']) # CHANGE AS NEEDED
    part1_ans = part1(contents)
    part2_ans = part2(contents)
    print(part1_ans)
    print(part2_ans)


if __name__ == "__main__":
    main()