def part1() -> int:
    file = open('1.txt', 'r')
    max_sum = 0
    curr_sum = 0
    
    for line in file:
        if line != '\n':
            curr_sum += int(line)
        else:
            max_sum = max(max_sum, curr_sum)
            curr_sum = 0
    
    max_sum = max(max_sum, curr_sum)
    
    return max_sum

def part2() -> int:
    file = open('1.txt', 'r')
    curr_sum = 0
    sums = []
    
    for line in file:
        if line != '\n':
            curr_sum += int(line)
        else:
            sums.append(curr_sum)
            curr_sum = 0
    
    sums.append(curr_sum)
    sums.sort(reverse=True)
    
    return sums[0] + sums[1] + sums[2]

def main():
    part1_ans = part1()
    part2_ans = part2()
    print(part2_ans)


if __name__ == "__main__":
    main()