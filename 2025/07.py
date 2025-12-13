import os
import time

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
    contents = read_file(this_filename, strip=False, delimiters=[''], line_range=(None, None)) # CHANGE AS NEEDED

    # splitters on every even indexed row
    # no splitters on the edge of the grid, so no bound check needed

    beam = [1 if space == 'S' else 0 for space in contents[0]]
    total_splits = 0
    for row in contents[2::2]:
        for i, space in enumerate(row):
            if space == '^' and beam[i] == 1:
                beam[i] = 0
                beam[i-1] = 1
                beam[i+1] = 1
                total_splits += 1
    
    return total_splits


def part2():
    """
    TODO: part 2 solution
    """
    contents = read_file(this_filename, strip=False, delimiters=[''], line_range=(None, None)) # CHANGE AS NEEDED

    beam = [1 if space == 'S' else 0 for space in contents[0]]
    for row in contents[2::2]:
        for i, space in enumerate(row):
            if space == '^' and beam[i] > 0:
                beams_to_split = beam[i]
                beam[i] = 0
                beam[i-1] += beams_to_split
                beam[i+1] += beams_to_split
    
    return sum(beam)

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