dirs = {
    "/": {
        "size": 0
    }
}
cwd = dirs["/"]

def chdir(cwd, newdir):
    if newdir == "/":
        cwd = dirs["/"]
    if newdir == "..":
        return cwd["parent"]
    cwd[newdir] = {
        "parent": cwd,
        
    }
        return cwd + "/" + newdir
    
def addup(path, amount):
    cwd = dirs['/']
    cwd['size'] += amount
    for dir in path.split('/'):
        cwd = cwd[dir]
        cws['size'] += amount
        
with open("input.txt") as f:
    curdir = "root"
    for line in f:
        tokens = line.strip().split()
        if tokens[0] == "$":
            if tokens[1] == "cd":
                curdir = chdir(curdir, tokens[2])
            else:
                continue
        elif tokens[0] == "dir":
            continue
        else:
            addup(curdir, int(tokens[0]))