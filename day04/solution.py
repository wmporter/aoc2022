fully_contained = 0

with open('input.txt') as f:
    for line in f:
        l1,r1,l2,r2 = line.strip().replace(',', ' ').replace('-', ' ').split()
        
        if (l1 >= l2 and r1 <= r2) or (l2 >= l1 and r2 <= r1):
            print(l1,r1,l2,r2)
            fully_contained += 1

print(fully_contained)