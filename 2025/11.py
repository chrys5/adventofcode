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
    contents = read_file(this_filename, strip=False, delimiters=[': ', ' '], line_range=(None, None)) # CHANGE AS NEEDED

    adj = {}
    for row in contents:
        adj[row[0]] = row[1:]
    
    # dfs from you to out
    stack = ['you']
    cache = {node: -1 for node in adj}
    visited = set()
    paths_to_out = 0
    while stack:
        curr = stack.pop()
        if curr == 'out':
            paths_to_out += 1
            continue
        cached_val = cache[curr]
        if cached_val != -1:
            paths_to_out += cached_val
            continue
        if curr in visited or curr not in adj:
            continue
        
        visited.add(curr)
        for nxt in adj[curr]:
            if nxt not in visited:
                stack.append(nxt)
        visited.remove(curr)
    return paths_to_out


def part2():
    """
    TODO: part 2 solution
    """
    contents = read_file(this_filename, strip=False, delimiters=[': ', ' '], line_range=(None, None)) # CHANGE AS NEEDED

    adj = {}
    for row in contents:
        adj[row[0]] = row[1:]
    
    ''' 
    4 states: no fft or dac, fft only, dac only, both fft and dac encountered

    dfs with caching to count paths to out based on current state
        for each node+state:
            return number of valid paths from node+state to out
            store in cache
    '''
    NUM_STATES = 4
    cache = {(node, state): -1 for state in range(NUM_STATES) for node in adj}
    visited = set()
    def dfs(node, state):
        if node == 'out':
            return 1 if state == NUM_STATES-1 else 0
        
        cached_val = cache[(node, state)]
        if cached_val != -1:
            return cached_val
        
        if node == 'fft':
            d_state = 1
        elif node == 'dac':
            d_state = 2
        else:
            d_state = 0
        
        state += d_state
        visited.add(node)

        paths_to_out = 0
        for nxt in adj[node]:
            if nxt not in visited:
                paths_to_out += dfs(nxt, state)
        cache[(node, state)] = paths_to_out
        
        visited.remove(node)
        state -= d_state
        return paths_to_out

    dfs('svr', 0)
    return cache[('svr', 0)]

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