import numpy as np

this_filename = '3.txt'

def read(filename: str):
    contents = None
    with open(filename, 'r') as f:
        contents = [line.strip() for line in f.readlines()]
    return contents

def part1():
    contents = read(this_filename)
    return None

def part2():
    contents = read(this_filename)
    
    return None

def main():
    part1_ans = part1()
    part2_ans = part2()
    print(part1_ans)
    print(part2_ans)


if __name__ == "__main__":
    main()