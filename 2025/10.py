import os
import time
import re
from collections import deque
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint

from utils import read_file

# filename should be absolute path name of this .py file with .txt extension
this_filename = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), 
    os.path.splitext(os.path.basename(__file__))[0] + '.txt')

light_regex = r'\[(.*?)\]'
button_regex = r'\((.*?)\)'
joltage_regex = r'\{(.*?)\}'

# -------------------------------------------------------------------------
def part1():
    """
    TODO: part 1 solution
    """
    contents = read_file(this_filename, strip=False, delimiters=None, line_range=(None, None)) # CHANGE AS NEEDED

    # convert to bitmasks
    machine_light_combos = []
    machine_light_goal = []
    machine_buttons = []
    for row in contents:
        lights_str = re.findall(light_regex, row)[0]
        buttons_str = re.findall(button_regex, row)

        machine_light_combos.append(2**len(lights_str))
        lights_bin = 0
        for i, light in enumerate(lights_str):
            if light == '#':
                lights_bin |= (1 << i)
        machine_light_goal.append(lights_bin)

        button_bins = []
        for button_str in buttons_str:
            buttons_int = [int(b) for b in button_str.split(',')]
            button_bin = 0
            for b in buttons_int:
                button_bin |= (1 << b)
            button_bins.append(button_bin)

        machine_buttons.append(button_bins)
    
    def bfs(light_combos, light_goal, buttons):
        light_start = 0
        if light_start == light_goal:
            return 0
        queue = deque()
        visited = [-1] * (light_combos + 1)
        visited[light_start] = 0
        queue.append((light_start, 0))
        while queue:
            curr_light, depth = queue.popleft()
            for button in buttons:
                next_light = curr_light ^ button
                if next_light == light_goal:
                    return depth + 1
                if visited[next_light] == -1:
                    visited[next_light] = depth + 1
                    queue.append((next_light, depth + 1))
        return None

    total_presses = 0
    # bfs on light and possible machine states
    for light_combos, light_goal, buttons in zip(machine_light_combos, machine_light_goal, machine_buttons):
        steps = bfs(light_combos, light_goal, buttons)
        if steps is None:
            return "ERROR"
        total_presses += steps

    return total_presses


def part2():
    """
    TODO: part 2 solution
    """
    contents = read_file(this_filename, strip=False, delimiters=None, line_range=(None, None)) # CHANGE AS NEEDED

    machine_joltage_goal = []
    machine_buttons = []
    for row in contents:
        buttons_str = re.findall(button_regex, row)
        joltage_str = re.findall(joltage_regex, row)[0]

        buttons = [tuple(int(b) for b in button_str.split(',')) for button_str in buttons_str]
        machine_buttons.append(buttons)

        joltages = tuple(int(j) for j in joltage_str.split(','))
        machine_joltage_goal.append(joltages)


    """
    solve linear optimization problem for each machine

    constraint: Ax = joltage
        A is a matrix where A[i][j] = 1 if button j increments joltage i
        x is a vector where x[j] = number of times button j is pressed
        joltage is a vector of target joltages
    
    objective: minimize cx (sum of x)
        c is vertical vector of 1s

    known bounds: 0 <= x <= max(joltage)
    """
    total_presses = 0
    for joltage, buttons in zip(machine_joltage_goal, machine_buttons):
        num_joltages = len(joltage)
        num_buttons = len(buttons)
        
        A = np.zeros((num_joltages, num_buttons), dtype=int)
        for b_idx, button in enumerate(buttons):
            for j_idx in button:
                A[j_idx][b_idx] = 1
        
        joltage = np.array(joltage, dtype=int).T
        c = np.ones(num_buttons, dtype=int)

        bounds = Bounds(0, max(joltage))
        constraint = LinearConstraint(A, joltage, joltage)
        result = milp(c, constraints=constraint, bounds=bounds, integrality=np.ones(num_buttons, dtype=int))

        if not result.success:
            return "ERROR"
        
        total_presses += result.fun

    return round(total_presses)

    
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