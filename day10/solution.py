with open("input.txt") as f:
    check = 20
    signal = 0
    cycle = 1
    x = 1
    for line in f:
        op = line.split()
        if op[0] == "noop":
            if cycle == check:
                signal += check * x
                print(f"{check}", check*x)
                check += 40
        if op[0] == "addx":
            if check in (cycle, cycle+1):
                signal += check * x
                print(f"{check}", check*x)
                check += 40
            cycle += 1
            print("x",x,"v",op[1])
            x += int(op[1])
        cycle += 1
print(signal)