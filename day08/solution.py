def check(val, trees):
    scenic = 0
    visible = True
    for tree in trees:
        scenic += 1
        if tree >= val:
            visible = False
            break
    return visible, scenic

def checkup(val, col, row):
    if row == 0:
        return True, 0
    return check(val, [trees[r][col] for r in range(row-1,-1,-1)])

def checkdown(val, col, row):
    if row == len(trees):
        return True, 0
    return check(val, [trees[r][col] for r in range(row+1,len(trees))])

def checkleft(val, col, row):
    if col == 0:
        return True, 0
    return check(val, trees[row][col-1::-1])

def checkright(val, col, row):
    if col == len(trees[0]):
        return True, 0
    return check(val, trees[row][col+1:])

def checkall(val, col, row):
    vup, sup = checkup(val, col, row)
    vdn, sdn = checkdown(val, col, row)
    vlt, slt = checkleft(val, col, row)
    vrt, srt = checkright(val, col, row)
    return (vup or vdn or vlt or vrt, sup * sdn * slt * srt)

trees = []
with open("input") as f:
    for line in f:
        trees.append(list(line.strip()))

visible = 0
scenic = 0
for r in range(len(trees[0])):
    for c in range(len(trees)):
        val = trees[r][c]
        vis, sce = checkall(val, c, r)
        visible += vis
        scenic = max(scenic, sce)

# part 1
print(visible)

# part 2
print(scenic)
