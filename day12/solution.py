from collections import deque

def bfs(g, start):
    
    unexplored = deque()
    unexplored.append(start)

    visited_from = {}
    visited_from[start[:-1]] = None

    while len(unexplored) > 0:
        cur = unexplored.popleft()
        for neighbor in g.neighbors(cur):
            if neighbor[:-1] not in visited_from:
                unexplored.append(neighbor)
                visited_from[neighbor[:-1]] = cur
    
    return visited_from


class Node:
    def __init__(self, r, c, el):
        self.r = r
        self.c = c
        self.el = el
    
    def tup(self):
        return self.r, self.c, self.el

class Grid:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.grid = {}

    def get(self, rowcol):
        return self.grid[rowcol]
    
    def neighbors(self, loc):
        (r, c, el) = loc
        result = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        result = filter(lambda n: 0 <= n[0] < self.h and 0 <= n[1] < self.w, result)
        result = filter(lambda n: ord(self.get(n)[2]) <= ord(el)+1, result)
        return map(self.get, result)

with open("input") as f:
    grid = {}
    for r, line in enumerate(f):
        for c, el in enumerate(line):
            if el == "S":
                n = (r, c, "a")
                start = n
            elif el == "E":
                n = (r, c, "z")
                end = n
            else:
                n = (r, c, el)
            grid[(r, c)] = n

    elf_map = Grid(len(line.strip()), r+1)
    elf_map.grid.update(grid)

visited_from = bfs(elf_map, start)

# part 1
cur = end
steps = 0
while cur != start:
    steps += 1
    cur = visited_from[cur[:-1]]
print(steps)

# part 2
cur = end
steps = 0
while cur[2] != 'a':
    steps += 1
    cur = visited_from[cur[:-1]]
print(steps)
