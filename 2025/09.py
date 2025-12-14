import os
import time
from collections import defaultdict

from utils import read_file

# filename should be absolute path name of this .py file with .txt extension
this_filename = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), 
    os.path.splitext(os.path.basename(__file__))[0] + '.txt')

# -------------------------------------------------------------------------
def part1():
    """
    TODO: part 1 solution
    """
    contents = read_file(this_filename, strip=False, delimiters=[','], line_range=(None, None)) # CHANGE AS NEEDED

    N = len(contents)

    coords = []
    for content in contents:
        coords.append(tuple(int(coord) for coord in content))
    
    max_rectangle = 0
    for i in range(N):
        for j in range(i+1, N):
            max_rectangle = max(max_rectangle, 
                                (abs(coords[i][0] - coords[j][0]) + 1) * (abs(coords[i][1] - coords[j][1]) + 1))

    return max_rectangle


def part2():
    """
    TODO: part 2 solution
    """
    contents = read_file(this_filename, strip=False, delimiters=[','], line_range=(None, None)) # CHANGE AS NEEDED

    N = len(contents)

    coords = []
    for content in contents:
        coords.append(tuple(int(coord) for coord in content))
    rectangles = []
    for i in range(N):
        for j in range(i+1, N):
            rectangles.append((
                (min(coords[i][0], coords[j][0]), min(coords[i][1], coords[j][1])),
                (max(coords[i][0], coords[j][0]), max(coords[i][1], coords[j][1]))
            ))
    # sort rectangles by area descending
    rectangles.sort(key=lambda rect: 
                    -(abs(rect[0][0] - rect[1][0]) + 1) * (abs(rect[0][1] - rect[1][1]) + 1))

    edges = []
    for i in range(1, N):
        edges.append((coords[i-1], coords[i]))
    edges.append((coords[N-1], coords[0]))
    # sort edges by length descending
    edges.sort(key=lambda edge: -max(abs(edge[0][0] - edge[1][0]), abs(edge[0][1] - edge[1][1])))

    # test every box. if box is intersected by any edge, it's not valid
    for rectangle in rectangles:
        corner_1_x, corner_1_y = rectangle[0]
        corner_2_x, corner_2_y = rectangle[1]
        valid = True

        for edge in edges:
            edge_1_x, edge_1_y = edge[0]
            edge_2_x, edge_2_y = edge[1]
            
            # check if edge is outside of rectangle
            if (max(edge_1_x, edge_2_x) <= min(corner_1_x, corner_2_x) or   # right
                min(edge_1_x, edge_2_x) >= max(corner_1_x, corner_2_x) or   # left
                max(edge_1_y, edge_2_y) <= min(corner_1_y, corner_2_y) or   # down
                min(edge_1_y, edge_2_y) >= max(corner_1_y, corner_2_y)):    # up
                continue
            else:
                valid = False
                break

        if valid:
            return (abs(corner_1_x - corner_2_x) + 1) * (abs(corner_1_y - corner_2_y) + 1)
    
    return 0
# -------------------------------------------------------------------------

def main():
    print("\nPart 1:")
    start_time = time.perf_counter()
    result1 = part1()
    end_time = time.perf_counter()
    print(result1)
    print(f"Runtime: {(end_time - start_time)*1000:.3f} ms")
    
    print("\nPart 2:")
    start_time = time.perf_counter()
    result2 = part2()
    end_time = time.perf_counter()
    print(result2)
    print(f"Runtime: {(end_time - start_time)*1000:.3f} ms")


if __name__ == "__main__":
    main()