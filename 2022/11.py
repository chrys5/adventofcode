from typing import List
import re
import os
from collections import deque
import sys


this_filename = '11.txt'


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


class Monkey:
    def __init__(self):
        self.items = None
        self.divide_by_3 = None
        self.operation = None
        self.test = None
        self.if_true = None
        self.if_false = None
        self.inspections = 0
    
    def __init_operation__(self, operator, op_const):
        if operator == '*':
            if op_const == 'old':
                self.operation = lambda old: (old * old) // (3 if self.divide_by_3 else 1)
            else:
                self.operation = lambda old: (old * int(op_const)) // (3 if self.divide_by_3 else 1)
        else:
            self.operation = lambda old: (old + int(op_const)) // (3 if self.divide_by_3 else 1)
    
    def __init_test__(self, divisor):
        self.test = lambda a: a % int(divisor) == 0

    def catch(self, item):
        self.items.append(item)
    
    def throw(self):
        return self.items.popleft()


class Item:
    def __init__(self, worry_level):
        self.worry_level = worry_level
    
    def update_worry_level(self, new_worry_level):
        self.worry_level = new_worry_level


def part1(contents: List[str]):
    """
    TODO: part 1 solution
    """
    global monkeys
    monkeys = []

    for i in range(0, len(contents), 7): #initialize monkeys
        str_starting_items, str_operation, str_test, str_if_true, str_if_false = contents[i+1:i+6]

        new_monkey = Monkey()
        
        new_monkey.items = deque([Item(int(item)) for item in str_starting_items[2:]])
        new_monkey.divide_by_3 = True
        new_monkey.__init_operation__(str_operation[-2], str_operation[-1])
        new_monkey.__init_test__(str_test[-1])
        new_monkey.if_true = int(str_if_true[-1])
        new_monkey.if_false = int(str_if_false[-1])

        monkeys.append(new_monkey)

    for round_num in range(20):
        for curr_monkey in monkeys:
            while curr_monkey.items:
                item = curr_monkey.throw()
                curr_monkey.inspections += 1
                item.update_worry_level(curr_monkey.operation(item.worry_level))
                if curr_monkey.test(item.worry_level):
                    dest_monkey = monkeys[curr_monkey.if_true]
                else:
                    dest_monkey = monkeys[curr_monkey.if_false]
                dest_monkey.catch(item)
    
    inspections = [monkey.inspections for monkey in monkeys]
    inspections.sort()
    
    return inspections[-1] * inspections[-2]


def part2(contents: List[str]):
    """
    TODO: part 2 solution
    """
    for monkey in monkeys:
        monkey.divide_by_3 = False
    
    for round_num in range(10000):
        print(str(round((round_num+1)/100, 2)) + '%', end='\r')

        for curr_monkey in monkeys:
            while curr_monkey.items:
                item = curr_monkey.throw()
                curr_monkey.inspections += 1
                item.update_worry_level(curr_monkey.operation(item.worry_level))
                if curr_monkey.test(item.worry_level):
                    dest_monkey = monkeys[curr_monkey.if_true]
                else:
                    dest_monkey = monkeys[curr_monkey.if_false]
                dest_monkey.catch(item)

    inspections = [monkey.inspections for monkey in monkeys]
    inspections.sort()
    
    return inspections[-1] * inspections[-2]


def main():
    contents = read(this_filename, start=1, stop=-1, splitting_enabled=True, delimiters=[' ', ',']) # CHANGE AS NEEDED
    part1_ans = part1(contents)
    print("Part 1: " + str(part1_ans))
    part2_ans = part2(contents)
    print("Part 2: " + str(part2_ans))


if __name__ == "__main__":
    main()