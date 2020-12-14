instructions = []

MASK = 'mask'
MEM = 'mem'

memory = dict()
current_mask = None


def update_memory(memory, value, mask, effective_value):
    floating_bits = [i for i in range(len(mask)) if mask[i] == 'X']

    value = int(mask.replace('X', '0'), 2) | value

    for i in range(2 ** len(floating_bits)):
        address = value

        for pos, j in enumerate(floating_bits):
            bit_value = i >> ((len(floating_bits) - 1 - pos)) & 1

            if bit_value == 1:
                address = address | (1 << (35 - j))
            else:
                address = address & ~(1 << (35 - j))

            memory[address] = effective_value


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
        update_memory(memory, instruction[1], current_mask, instruction[2])

s = 0
for k, v in memory.items():
    s += v

print(s)
