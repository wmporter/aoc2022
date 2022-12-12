import math

def Dijkstra(graph, source):

    q = queue()
    for row in graph:
        for v in row:
            v.dist = math.inf
            if v is source:
                v.dist = 0
            v.prev = None
            q.add(v)
    # source.dist = 0

    while q.q:
        u = q.remove()
        print(f"{u.dist=}")
        for v in u.neighbors:
            # print(v.dist)
            if v in q.q:
                alt = u.dist + 1
                # print(alt)
                if alt < v.dist:
                    v.dist = alt
                    v.prev = u
                    # print(v)

class queue:
    def __init__(self):
        self.q = []
    def add(self, v):
        for i in range(len(self.q)-1, -1, -1):
            if v.dist >= self.q[i].dist:
                self.q.insert(i, v)
                return
        self.q.insert(0, v)
    def remove(self):
        return self.q.pop(0)

class Node:
    pass
    def add_neighbor(self, neighbor):
        if ord(self.el) - ord(neighbor.el) >= -1:
            self.neighbors.append(neighbor)
    def __repr__(self):
        return self.el

grid = []
with open("sminput") as f:
    for line in f:
        row = []
        for el in line.strip():
            n = Node()
            if el == "S":
                n.el = "a"
                start = n
            elif el == "E":
                n.el = "z"
                end = n
            else:
                n.el = el
            row.append(n)
        grid.append(row)

R = len(grid)-1
print(grid)
C = len(grid[0])-1

for r in range(R+1):
    for c in range(C+1):
            node = grid[r][c]
            node.neighbors = []
            if r == 0:
                node.add_neighbor(grid[r+1][c])
            elif r == R:
                node.add_neighbor(grid[r-1][c])
            else:
                node.add_neighbor(grid[r-1][c])
                node.add_neighbor(grid[r+1][c])

            if c == 0:
                node.add_neighbor(grid[r][c+1])
            elif c == C:
                node.add_neighbor(grid[r][c-1])
            else:
                node.add_neighbor(grid[r][c-1])
                node.add_neighbor(grid[r][c+1])

print(grid[2][4].neighbors)
Dijkstra(grid, start)
print(end.dist)
