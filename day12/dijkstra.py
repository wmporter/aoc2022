import math

# simple graph node
class Node:
    pass
    def add_neighbor(self, neighbor):
        if ord(self.el) - ord(neighbor.el) >= -1:
            self.neighbors.append(neighbor)
    def __repr__(self):
        return self.el

# min priority queue implementation for dijkstra
class queue:
    def __init__(self):
        self.q = []
    
    def add(self, v):
        for i in range(len(self.q)):
            if v.dist < self.q[i].dist:
                self.q.insert(i, v)
                return
        self.q.append(v)
    
    def remove(self):
        return self.q.pop(0)
    
    # need to call this whenever dist value changes for any node in the queue
    # to keep it in min priority order
    def update(self, v):
        self.q.pop(self.q.index(v))
        self.add(v)

# modified dijkstra algorithm
def dijkstra(graph, source, short_circuit=False):

    q = queue()
    for row in graph:
        for v in row:
            v.dist = math.inf
            v.prev = None
            q.add(v)
    source.dist = 0
    q.update(source)

    while q.q:
        u = q.remove()
        for v in u.neighbors:
            if short_circuit and v.el == "a":
                return False
            if v in q.q:
                alt = u.dist + 1  # all edges are 1
                if alt < v.dist:
                    v.dist = alt
                    v.prev = u
                    q.update(v)
    return True


grid = []
start_options = []
with open("input") as f:
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
                if el == "a":
                    start_options.append(n)
            row.append(n)
        grid.append(row)

R = len(grid)-1
C = len(grid[0])-1

for r in range(R+1):
    for c in range(C+1):
            node = grid[r][c]
            node.neighbors = []
            if node is end:
                continue
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

dijkstra(grid, start)
print(end.dist)
