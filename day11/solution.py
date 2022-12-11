import re, operator

class Monkey:
    items = None
    oper = None
    test = None
    trueact = None
    falseact = None
    inspect = 0
    
def operate(operation, value):
    op,rhs = operation.split()
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
with open("input.txt") as f:
    for line in f:
        items = re.search(r": (.*)$", next(f).strip()).group(1)
        oper = re.search(r"= old (.*)$", next(f).strip()).group(1)
        test = re.search(r"(\d+)$", next(f).strip()).group(1)
        trueact = re.search(r"(\d+)$", next(f).strip()).group(1)
        falseact = re.search(r"(\d+)$", next(f).strip()).group(1)
        
        m = Monkey()
        m.items = list(map(int, items.split(",")))
        m.oper = oper
        m.test = int(test)
        m.trueact = int(trueact)
        m.falseact = int(falseact)
        monkeys.append(m)
        
        # skip blank line
        next(f)

for round in range(20):
    for monkey in monkeys:
        for item in monkey.items:
            item = operate(monkey.oper, item) // 3
            monkey.inspect += 1
            if item % monkey.test == 0:
                monkeys[monkey.trueact].items.append(item)
            else:
                monkeys[monkey.falseact].items.append(item)

print(monkeys[0].items)