import re

def get_columns(line):
    col = 1
    values = {}
    while True:
        if line[col] != " ":
            values[(col-1)//4+1] = line[col]
        col += 4
        if col >= len(line):
            break
    return values

def move(stacks, amount, fr, to):
    for _ in range(amount):
        v = stacks[fr].pop(0)
        stacks[to].insert(0, v)

def move_as_one(stacks, amount, fr, to):
    stacks[to] = stacks[fr][:amount] + stacks[to]
    stacks[fr] = stacks[fr][amount:]


with open('input') as f:
    stacks = {}
    stacks_new = {}
    for line in f:
        if '[' in line:
            col = get_columns(line)
            for k in col:
                if k in stacks:
                    stacks[k].append(col[k])
                    stacks_new[k].append(col[k])
                else:
                    stacks[k] = [col[k]]
                    stacks_new[k] = [col[k]]
        else:
            break

    # skip the blank line
    next(f)

    for line in f:
        values = re.match(r'move (\d+) from (\d+) to (\d+)', line).groups()
        move(stacks, *map(int, values))
        move_as_one(stacks_new, *map(int, values))

# part 1
print("".join(s[0] for s in stacks.values()))

# part 2
print("".join(s[0] for s in stacks_new.values()))
