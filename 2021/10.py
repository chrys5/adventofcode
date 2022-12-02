#practice

from collections import deque

this_filename = 'practice.txt'

def read(filename: str):
    contents = None
    with open(filename, 'r') as f:
        contents = [line.strip() for line in f.readlines()]
    return contents

def part1():
    contents = read(this_filename)

    score = {')': 3, ']': 57, '}': 1197, '>': 25137}
    open_close = {'(': ')', '[': ']', '{': '}', '<': '>'}
    stack = deque()

    sum = 0
    for line in contents:
        for char in line:
            if char in open_close:
                stack.append(open_close[char])
            elif char != stack.pop():
                sum += score[char]
                break

    return sum

def part2():
    contents = read(this_filename)

    score = {')': 1, ']': 2, '}': 3, '>': 4}
    open_close = {'(': ')', '[': ']', '{': '}', '<': '>'}
    
    scores = []
    for line in contents:
        stack = deque()
        corrupt = False
        for char in line:
            if char in open_close:
                stack.append(open_close[char])
            elif stack and char != stack.pop():
                corrupt = True
                break
        if not corrupt:
            curr_score = 0
            while stack:
                curr_score = curr_score * 5 + score[stack.pop()]
            scores.append(curr_score)

    scores.sort()

    print(scores)

    return scores[len(scores) // 2]

def main():
    part1_ans = part1()
    part2_ans = part2()
    print(part1_ans)
    print(part2_ans)


if __name__ == "__main__":
    main()