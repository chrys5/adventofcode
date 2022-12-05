from collections import deque
import re
import string

this_filename = '5.txt'

def read(filename: str):
    contents = None
    with open(filename, 'r') as f:
        contents = [line.strip() for line in f.readlines()]
    return contents

def part1():
    contents = read(this_filename)
    stacks = []
    for i in range(9):
        stacks.append(deque())
    elements = ['BQC', 
                'RQWZ',
                'BMRLV',
                'CZHVTW',
                'DZHBNVG',
                'HNPCJFVQ',
                'DGTRWZS',
                'CGMNBWZP',
                'NJBMWQFP']
    for i in range(9):
        for char in elements[i]:
            stacks[i].append(char)

    for line in contents[10:]:
        line_elements = re.split(r'move | from | to ', line)
        amount, a, b = [int(element) for element in line_elements if element != '']
        for i in range(amount):
            stacks[b-1].append(stacks[a-1].pop())

    ret_string = ''
    for stack in stacks:
        ret_string += stack[-1]
    
    return ret_string

def part2():
    contents = read(this_filename)
    stacks = []
    for i in range(9):
        stacks.append(deque())
    elements = ['BQC', 
                'RQWZ',
                'BMRLV',
                'CZHVTW',
                'DZHBNVG',
                'HNPCJFVQ',
                'DGTRWZS',
                'CGMNBWZP',
                'NJBMWQFP']
    for i in range(9):
        for char in elements[i]:
            stacks[i].append(char)

    for line in contents[10:]:
        line_elements = re.split(r'move | from | to ', line)
        amount, a, b = [int(element) for element in line_elements if element != '']
        temp_stack = deque()
        for i in range(amount):
            temp_stack.append(stacks[a-1].pop())
        for i in range(amount):
            stacks[b-1].append(temp_stack.pop())

    ret_string = ''
    for stack in stacks:
        ret_string += stack[-1]
    
    return ret_string

def main():
    part1_ans = part1()
    part2_ans = part2()
    print(part1_ans)
    print(part2_ans)


if __name__ == "__main__":
    main()