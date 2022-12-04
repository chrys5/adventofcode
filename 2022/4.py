import re

this_filename = '4.txt'

def read(filename: str):
    contents = None
    with open(filename, 'r') as f:
        contents = [line.strip() for line in f.readlines()]
    return contents

def part1():
    contents = read(this_filename)
    sum = 0
    for line in contents:
        line_elements = re.split(r',|-', line)
        nums = [int(element) for element in line_elements]
        if nums[0] <= nums[2] and nums[1] >= nums[3]:
            sum += 1
        elif nums[0] >= nums[2] and nums[1] <= nums[3]:
            sum += 1
    return sum

def part2():
    contents = read(this_filename)
    sum = 0
    for line in contents:
        line_elements = re.split(r',|-', line)
        nums = [int(element) for element in line_elements]
        if nums[0] < nums[2] and nums[1] < nums[2]:
            sum += 0
        elif nums[2] < nums[0] and nums[3] < nums[0]:
            sum += 0
        else:
            sum += 1
    return sum

def main():
    part1_ans = part1()
    part2_ans = part2()
    print(part1_ans)
    print(part2_ans)


if __name__ == "__main__":
    main()