def move_tail(tx, ty, hx, hy):
    ydiff = ty - hy
    xdiff = tx - hx

    # touching so no movement
    if abs(ydiff)<=1 and abs(xdiff)<=1:
        return (0, 0)

    xmove = ymove = 0
    if ydiff != 0:
        ymove = (-ydiff)//abs(ydiff)
    if xdiff != 0:
        xmove = (-xdiff)//abs(xdiff)

    return xmove, ymove


lrud = {
    "L": (-1, 0),
    "R": (1, 0),
    "U": (0, 1),
    "D": (0, -1)
}
h = (0,0)
knots = {
    1: (0,0),
    2: (0,0),
    3: (0,0),
    4: (0,0),
    5: (0,0),
    6: (0,0),
    7: (0,0),
    8: (0,0),
    9: (0,0),
}
vis1 = {(0,0)}
vis9 = {(0,0)}

with open("input") as f:
    for line in f:
        d, n = line.strip().split()

        for _ in range(int(n)):
            # move head
            hx, hy = h
            dx, dy = lrud[d]
            h = (hx+dx, hy+dy)

            # move tails
            prev = h
            for i in range(1,10):
                mx, my = move_tail(*knots[i], *prev)
                knots[i] = (knots[i][0]+mx, knots[i][1]+my)
                prev = knots[i]

            vis1.add(knots[1])
            vis9.add(knots[9])

print(len(vis1))
print(len(vis9))
