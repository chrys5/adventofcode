this_filename = '03.txt'

def read(filename: str):
    contents = None
    with open(filename, 'r') as f:
        contents = [line.strip() for line in f.readlines()]
    return contents

def part1():
    contents = read(this_filename)
    sum = 0
    letters = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for line in contents:
        set1 = set()
        set2 = set()
        for i in range(len(line) // 2):
            set1.add(line[i])
            set2.add(line[len(line) // 2 + i])
        for letter in set1:
            if letter in set2:
                sum += letters.index(letter)
    
    return sum

def part2():
    contents = read(this_filename)
    sum = 0
    letters = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(0, len(contents), 3):
        set1 = set()
        set2 = set()
        set3 = set()
        for letter in contents[i]:
            set1.add(letter)
        for letter in contents[i+1]:
            set2.add(letter)
        for letter in contents[i+2]:
            set3.add(letter)
        for letter in set1:
            if letter in set2 and letter in set3:
                sum += letters.index(letter)
                break
    
    return sum

def main():
    part1_ans = part1()
    part2_ans = part2()
    print(part1_ans)
    print(part2_ans)


if __name__ == "__main__":
    main()