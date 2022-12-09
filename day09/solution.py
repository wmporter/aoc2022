def move_taik(tail, head):
    if abs(tail[0]-head[0])<=1 and abs(taik[1]-head[1])<=1:
        return tail
    tx, ty = tail
    hx, hy = head
    if ty-hy == 1:
        
        
    
    
lrud = {
    "L": (-1, 0),
    "R": (1, 0),
    "U": (0, 1),
    "D": (0, -1)
}    
h = (0,0)
t = (0,0)
vis = {(0,0)}

with open("input.txt") as f:
    for line in f:
        d, n = line.strip().split()
        hx, hy = h
        dx, dy = lrud[d]
        h = (hx+dx, hy+dy)
        t = move_tail(t, h)
        vis.add(t)
        
print(len(vis))