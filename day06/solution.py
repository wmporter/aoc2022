def dupes(segment):
    return len(segment) != len(set(segment))
    
with open("input.txt") as f:
    code = f.read()
    
packet = None
message = None
for i in range(len(code)-4):
    if packet is None and not dupes(code[i:i+4]):
        packet = i+4
    if message is None and not dupes(code[i:i+14]):
        message = i+14
    if packet and message:
        break
     
# part 1
print(packet)

# part 2
print(message)