fully_contained = 0
overlapped = 0

with open('input') as f:
    for line in f:
        l1,r1,l2,r2 = map(int, line.strip().replace(',', ' ').replace('-', ' ').split())

        if r1 < l2 or r2 < l1:
            continue

        if (l1 >= l2 and r1 <= r2) or (l2 >= l1 and r2 <= r1):
            fully_contained += 1

        overlapped += 1

# part 1
print(fully_contained)

# part 2
print(overlapped)
