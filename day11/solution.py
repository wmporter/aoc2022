import re, operator

class Monkey:
    original_items = None
    oper = None
    test = None
    trueact = None
    falseact = None

def operate(operation, value):
    op, rhs = operation.split()
    if rhs == "old":
        rhs = value
    else:
        rhs = int(rhs)
    ops = {
        "+": operator.add,
        "*": operator.mul
    }
    return ops[op](value, rhs)

monkeys = []
worry_reducer = 1
with open("input") as f:
    for line in f:
        items = re.search(r": (.*)$", next(f).strip()).group(1)
        oper = re.search(r"= old (.*)$", next(f).strip()).group(1)
        test = re.search(r"(\d+)$", next(f).strip()).group(1)
        worry_reducer = worry_reducer * int(test)
        trueact = re.search(r"(\d+)$", next(f).strip()).group(1)
        falseact = re.search(r"(\d+)$", next(f).strip()).group(1)

        m = Monkey()
        m.original_items = list(map(int, items.split(",")))
        m.oper = oper
        m.test = int(test)
        m.trueact = int(trueact)
        m.falseact = int(falseact)
        monkeys.append(m)

        # skip blank line
        try:
            next(f)
        except StopIteration:
            break

# reset inspections
for monkey in monkeys:
    monkey.inspect = 0
    monkey.items = monkey.original_items[:]

for round in range(20):
    for monkey in monkeys:
        while monkey.items:
            item = monkey.items.pop(0)
            item = operate(monkey.oper, item) // 3
            monkey.inspect += 1
            if item % monkey.test == 0:
                monkeys[monkey.trueact].items.append(item)
            else:
                monkeys[monkey.falseact].items.append(item)

part1monkeys = sorted(monkeys, key=lambda m: m.inspect)
print(part1monkeys[-1].inspect * part1monkeys[-2].inspect)

# reset inspections
for monkey in monkeys:
    monkey.inspect = 0
    monkey.items = monkey.original_items[:]

for round in range(10000):
    for monkey in monkeys:
        while monkey.items:
            item = monkey.items.pop(0)
            item = operate(monkey.oper, item) % worry_reducer
            monkey.inspect += 1
            if item % monkey.test == 0:
                monkeys[monkey.trueact].items.append(item)
            else:
                monkeys[monkey.falseact].items.append(item)

part2monkeys = sorted(monkeys, key=lambda m: m.inspect)
print(part2monkeys[-1].inspect * part2monkeys[-2].inspect)
