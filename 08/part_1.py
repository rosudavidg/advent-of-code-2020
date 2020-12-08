lines = []

instructions = []

with open('file.in', 'rt') as fin:
    for line in list(map(lambda l: l.strip(), fin.readlines())):
        instructions.append(
            [False, line.split(' ')[0], int(line.split(' ')[1])])

acc = 0
index = -1

while True:
    index += 1
    instruction = instructions[index]

    if instruction[0]:
        break
    else:
        instruction[0] = True

    if instruction[1] == 'nop':
        continue
    elif instruction[1] == 'acc':
        acc += instruction[2]
    elif instruction[1] == 'jmp':
        index += instruction[2] - 1

print(acc)
