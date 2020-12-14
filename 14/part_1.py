instructions = []

MASK = 'mask'
MEM = 'mem'

memory = dict()
current_mask = None


with open('file.in', 'rt') as fin:
    for line in fin.readlines():
        k, v = list(map(lambda s: s.strip(), line.split('=')))

        if k == MASK:
            instructions.append((MASK, v))
        else:
            k = k.split('[')[1][:-1]
            instructions.append((MEM, int(k), int(v)))


for instruction in instructions:
    if instruction[0] == MASK:
        current_mask = instruction[1]
    else:
        memory[instruction[1]] = int(current_mask.replace(
            'X', '1'), 2) & instruction[2] | int(current_mask.replace('X', '0'), 2)

s = 0
for k, v in memory.items():
    s += v

print(s)
