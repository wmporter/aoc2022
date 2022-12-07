dirs = {
    "/": {
        "size": 0,
        "parent": None
    }
}
cwd = dirs["/"]

def chdir(newdir):
    global cwd
    if newdir == "/":
        cwd = dirs["/"]
    elif newdir == "..":
        cwd = cwd["parent"]
    elif newdir not in cwd:
        cwd[newdir] = {
            "parent": cwd,
            "size": 0,
        }
        cwd = cwd[newdir]
    
def addup(amount):
    cwd['size'] += amount
    p = cwd['parent']
    while p:
        p['size'] += amount
        p = p['parent']

def sumsmall(dir):
    sumthis = 0
    if dir["size"] <= 100000:
        sumthis = dir["size"]
    for subdir in dir:
        if subdir in ("size", "parent"):
            continue
        sumthis += sumsmall(dir[subdir])
    return sumthis

def leastbig(dir, amount):
    if dir["size"] < amount:
        return None

    least = dir["size"]
    for subdir in dir:
        if subdir in ("size", "parent"):
            continue
        potential_least = leastbig(dir[subdir], amount)
        if potential_least and potential_least < least:
            least = potential_least
    return least

with open("input") as f:
    for line in f:
        tokens = line.strip().split()
        if tokens[0] == "$":
            if tokens[1] == "cd":
                chdir(tokens[2])
            else:
                continue
        elif tokens[0] == "dir":
            continue
        else:
            addup(int(tokens[0]))

# part 1
print(sumsmall(dirs["/"]))

# part 2
print(leastbig(dirs["/"], dirs["/"]["size"]-40000000))
