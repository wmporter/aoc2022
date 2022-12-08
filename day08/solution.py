def checkup(val, col, row):
    return max([trees[r][col] for r in range(row)]) < val
    
def checkdown(val, col, row):
    return max([trees[r][col] for r in range(row+1,len(trees))]) < val
    
def checkleft(val, col, row):
    return max(trees[row][:col]) < val
    
def checkright(val, col, row):
    return max(trees[row][col+1:]) < val
    

trees = []
with open("input.txt") as f:
    for line in f:
        trees.append(list(line.strip()))

visible = 2 * (len(trees) + len(trees[0])) - 4
for r in range(1,len(trees[0])-1):
    for c in range(1, len(trees)-1):
        val = trees[r][c]
        if checkup(val, c, r) or checkdown(val, c, r) or checkleft(val, c, r) or checkright(val, c, r):
            visible += 1
            
print(visible)