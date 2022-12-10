def pixel(p, x):
    if p % 40 in (x-1, x, x+1):
        return "#"
    return "."

with open("input") as f:
    check = 20
    signal = 0
    cycle = 1
    screen = ""
    x = 1

    for line in f:
        op = line.split()

        screen += pixel(cycle-1, x)
        if cycle % 40 == 0:
            screen += "\n"

        if op[0] == "noop":
            if cycle == check:
                signal += check * x
                check += 40

        if op[0] == "addx":
            if check in (cycle, cycle+1):
                signal += check * x
                check += 40
            cycle += 1
            screen += pixel(cycle-1, x)
            if cycle % 40 == 0:
                screen += "\n"
            x += int(op[1])

        cycle += 1

# part 1
print(signal)

# part 2
print(screen)
