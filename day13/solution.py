import json

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return 0 if left == right else (-1 if left < right else 1)

    if isinstance(left, list) and isinstance(right, list):
        for i in range(len(left)):
            # right ran out of items first
            if i >= len(right):
                return 1
            c = compare(left[i], right[i])
            if c == 0:
                continue
            return c

        if len(right) == len(left):
            return 0
        return -1

    if isinstance(left, int):
        return compare([left], right)
    
    if isinstance(right, int):
        return compare(left, [right])

with open("input") as f:
    pair = 1
    pairs = []
    for line in f:
        left = json.loads(line.strip())
        right = json.loads(next(f).strip())
        pairs.append(pair if compare(left, right) < 0 else 0)
        try:
            next(f)
        except:
            break
        pair += 1
    
print(sum(pairs))