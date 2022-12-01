elves = []
with open('input') as f:
    calories = 0
    for line in f:
        line = line.strip()
        if line:
            calories += int(line)
        else:
            elves.append(calories)
            calories = 0

elves.sort()

# part 1
print(elves[-1])

# part 2
print(sum(elves[-3:]))
