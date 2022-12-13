import math

class Node:
    def __init__(self):
        self.neighbors = []

    def __repr__(self):
        return f"Node: ({self.r}, {self.c}) el: {self.el}"
    def add_neighbor(self, n):
        self.neighbors.append(n)

    # def valid_neighbors(self):
    #     return filter(lambda n: self.el - n.el <= 1, self.neighbors)
        # for neighbor in node.neighbors:
        #     if node.el - neighbor.el <= -1

class Tree:
    root = None

    def valid_neighbors(self, node):
        return filter(lambda n: node.el - n.el >= -1, node.neighbors)
        # for neighbor in node.neighbors:
        #     if node.el - neighbor.el <= -1
    
    def traverse_back(self, node, seen, step=0):
        
        if node.el == 1:
            return 1
        else:
            minimum = math.inf
            min_node = None
            
            print("neighbors", neighbors)
            if not neighbors: return math.inf
            for neighbor in neighbors:
                if neighbor in seen:
                    continue
                path = self.traverse_back(neighbor, seen + [node], 1)
                if path < minimum:
                    minimum = path
                    min_node = neighbor
            return minimum + step

    def traverse(self, node, seen, step=0):
        print(node)
        # if node in seen:
        #     return math.inf
        # elif node is end:
        if node is end:
            # print(node)
            return 1
        else:
            # seen.append(node)
            # path = math.inf
            # for neighbor in self.valid_neighbors(node):
            #     tail = self.traverse(neighbor, seen + [node])
            #     path = min(
            #         path = tail
            #     # print(path)
            # # return path
            print(node)
            minimum = math.inf
            min_node = None
            neighbors = list(self.valid_neighbors(node))
            print("neighbors", neighbors)
            if not neighbors: return math.inf
            for neighbor in neighbors:
                if neighbor in seen:
                    continue
                path = self.traverse(neighbor, seen + [node], 1)
                if path < minimum:
                    minimum = path
                    min_node = neighbor
            # if min_node:
            #     print(f"{minimum=} {min_node=}")
            return minimum + step
            # return min(map(lambda n: self.traverse(n, seen + [node]), neighbors)) + step

grid = []
with open("input") as f:
    for r, line in enumerate(f):
        row = []
        for c, el in enumerate(line.strip()):
            n = Node()
            n.r = r
            n.c = c
            if el == "S":
                n.el = 1
                start = n
            elif el == "E":
                n.el = 26
                end = n
            else:
                # print(el)
                n.el = ord(el) - ord("a") + 1
                # if el == "a":
                #     start_options.append(n)
            # print(n)
            row.append(n)
        grid.append(row)

R = len(grid)-1
C = len(grid[0])-1

for r in range(R+1):
    for c in range(C+1):
            node = grid[r][c]
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

print(Tree().traverse(start, [start]))
# print(Tree().traverse_back(end, [end]))