import string

priorities = string.ascii_lowercase + string.ascii_uppercase

def pri_error(sack):
    mid = len(sack) // 2
    error = (set(sack[:mid]) & set(sack[mid:])).pop()
    return priorities.index(error) + 1

def badge(sacks):
    result = set(sacks[0])
    for sack in sacks[1:]:
        result &= set(sack)
    return priorities.index(result.pop()) + 1

with open('input') as f:
    error_sum = 0
    badge_sum = 0
    for line in f:
        sack_group = [line.strip(), next(f).strip(), next(f).strip()]
        error_sum += sum([pri_error(sack) for sack in sack_group])
        badge_sum += badge(sack_group)

# part 1
print(error_sum)

# part 2
print(badge_sum)
