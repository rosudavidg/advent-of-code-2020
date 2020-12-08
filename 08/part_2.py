import copy

lines = []
instructions = []

with open('file.in', 'rt') as fin:
    for line in list(map(lambda l: l.strip(), fin.readlines())):
        instructions.append(
            [False, line.split(' ')[0], int(line.split(' ')[1])])


for i in range(len(instructions)):
    aux_instructions = copy.deepcopy(instructions)

    if aux_instructions[i][1] == 'nop':
        aux_instructions[i][1] = 'jmp'
    elif aux_instructions[i][1] == 'jmp':
        aux_instructions[i][1] = 'nop'

    acc = 0
    index = -1

    while index != len(instructions) - 1:
        index += 1
        instruction = aux_instructions[index]

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

    if index == len(instructions) - 1:
        print(acc)
        break
