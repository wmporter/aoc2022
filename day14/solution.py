def draw(blocks, left, right, bottom):
    for r in range(bottom+1):
        for c in range(left, right+1):
            if (c,r) in blocks:
                print(blocks[(c,r)], end='')
            else:
                print(" ", end='')
        print()

def set_walls(points):
    walls = {}
    for entry in points:
        for i in range(len(entry)-1):
            (x1, y1) = entry[i]
            (x2, y2) = entry[i+1]
            if x1 == x2:
                for y in range(min(y1,y2), max(y1,y2)+1):
                    # for appearances, don't replace floor with wall
                    if (x1, y) not in walls:
                        walls[(x1, y)] = "|"
            else:
                for x in range(min(x1,x2), max(x1,x2)+1):
                    walls[(x, y1)] = "-"
    return walls

def sand(walls, start, end):
    if start in walls:
        return False
    (x, y) = start
    while True:
        if (x, y+1) not in walls:
            y += 1
        elif (x-1, y+1) not in walls:
            x -= 1
            y += 1
        elif (x+1, y+1) not in walls:
            x += 1
            y += 1
        else:
            walls[(x, y)] = "."
            return True
        
        if y == end:
            return False

with open("input") as f:
    points = []
    xmin = xmax = 500
    ymax = 0
    for line in f:
        endpoints = [tuple(map(int, p.split(","))) for p in line.strip().split(" -> ")]
        xs, ys = zip(*endpoints)
        xmin = min(xmin, *xs)
        xmax = max(xmax, *xs)
        ymax = max(ymax, *ys)
        points.append(endpoints)

floorx = (500-ymax-3, 500+ymax+3)
floory = ymax+2
floor = [(floorx[0], floory), (floorx[1], floory)]

# part 1
walls = set_walls(points)

grains = 0
while True:
    if sand(walls, start=(500, 0), end=ymax):
        grains += 1
        continue
    break
print(grains)

# part 2
points.append(floor)
walls = set_walls(points)

grains = 0
while True:
    if sand(walls, start=(500, 0), end=0):
        grains += 1
        continue
    break
print(grains)
    