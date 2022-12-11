def part1() -> int:
    file = open('02.txt', 'r')
    input = []
    idx = {'A': 0, 'B': 1, 'C': 2, 'X': 0, 'Y': 1, 'Z': 2}
    outcomes = [[3, 6, 0],
                [0, 3, 6],
                [6, 0, 3]]
    handbonus = [1, 2, 3]
    
    for line in file:
        input.append([idx[line[0]], idx[line[2]]])
    
    sum = 0
    for a, b in input:
        sum += outcomes[a][b] + handbonus[a]
    
    return sum

def part2() -> int:
    file = open('02.txt', 'r')
    input = []
    idx = {'A': 0, 'B': 1, 'C': 2, 'X': 0, 'Y': 1, 'Z': 2}
    
    for line in file:
        input.append([idx[line[0]], idx[line[2]]])

    
    outcomes = [[3, 6, 0],
                [0, 3, 6],
                [6, 0, 3]]
    handbonus = [1, 2, 3]

    whatami = [
                [2, 0, 1],
                [0, 1, 2],
                [1, 2, 0]
                ]
    
    sum = 0
    for a, b in input:
        me = whatami[a][b]
        sum += outcomes[a][me] + handbonus[me]
    
    return sum


def main():
    part1_ans = part1()
    part2_ans = part2()
    print(part2_ans)


if __name__ == "__main__":
    main()