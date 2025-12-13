import os
import time
import numpy as np
import heapq
from collections import defaultdict

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
    contents = read_file(this_filename, strip=False, delimiters=[','], line_range=(None, None)) # CHANGE AS NEEDED

    N = len(contents)
    k = 1000    # number of closest pairs to consider
    k2 = 3      # number of largest circuits to find

    box_locations = []
    for content in contents:
        box_locations.append(tuple(int(coord) for coord in content))

    # compute all pairwise distances
    pair_dists = []
    for i in range(N):
        for j in range(i+1, N):
            dist = sum((a - b) ** 2 for a, b in zip(box_locations[i], box_locations[j]))
            if len(pair_dists) < k:
                heapq.heappush(pair_dists, (-dist, i, j))
            elif dist < -pair_dists[0][0]:
                heapq.heapreplace(pair_dists, (-dist, i, j))
    
    # build graph
    pair_dists = [(-d, i, j) for d, i, j in pair_dists]
    adj = defaultdict(list)
    for dist, i, j in pair_dists:
        adj[i].append(j)
        adj[j].append(i)
    
    # define dfs to find connected components
    visited = set()
    def dfs(node):
        stack = [node]
        size = 0
        while stack:
            curr = stack.pop()
            if curr in visited:
                continue
            visited.add(curr)
            size += 1
            for nxt in adj[curr]:
                if nxt not in visited:
                    stack.append(nxt)
        return size

    # find sizes of all connected components, add to max-heap
    sizes = []
    for node in adj.keys():
        if node not in visited:
            circuit_size = dfs(node)
            heapq.heappush(sizes, -circuit_size)
    ret = 1
    for _ in range(k2):
        ret *= -heapq.heappop(sizes)
    
    return ret


def part2():
    """
    TODO: part 2 solution
    """
    contents = read_file(this_filename, strip=False, delimiters=[','], line_range=(None, None)) # CHANGE AS NEEDED

    N = len(contents)

    box_locations = []
    for content in contents:
        box_locations.append(tuple(int(coord) for coord in content))

    # compute all pairwise distances
    pair_dists = []
    for i in range(N):
        for j in range(i+1, N):
            dist = sum((a - b) ** 2 for a, b in zip(box_locations[i], box_locations[j]))
            heapq.heappush(pair_dists, (dist, i, j))

    # union find with optimizations
    parent = [-1] * N
    size = [1] * N # size should be how nodes are connected
    global_root = pair_dists[0][1]
    visited = set()

    def find(node):
        if parent[node] == -1:
            return node
        parent[node] = find(parent[node])
        return parent[node]
    def union(node_1, node_2):
        nonlocal global_root
        root_1, root_2 = find(node_1), find(node_2)
        if root_1 != root_2:
            if size[root_1] < size[root_2]:
                parent[root_1] = root_2
                size[root_2] += size[root_1]
                if root_1 == global_root:
                    global_root = root_2
            else:
                parent[root_2] = root_1
                size[root_1] += size[root_2]
                if root_2 == global_root:
                    global_root = root_1
        
    last_connection = pair_dists[0]
    while size[global_root] < N:
        _, i, j = heapq.heappop(pair_dists)
        union(i, j)
        visited.add(i)
        visited.add(j)
        last_connection = (_, i, j)
    
    x1 = box_locations[last_connection[1]][0]
    x2 = box_locations[last_connection[2]][0]
    return x1 * x2

    
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