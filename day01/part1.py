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

print(max(elves))
