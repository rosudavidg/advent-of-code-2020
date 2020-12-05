lines = []

with open('file.in', 'rt') as fin:
    lines = list(map(lambda l: l.strip(), fin.readlines()))

values = []

for line in lines:
    row = int(line[:7].replace('F', '0').replace('B', '1'), 2)
    column = int(line[7:].replace('L', '0').replace('R', '1'), 2)

    values.append(row * 8 + column)

values.sort()

for i in range(len(values)):
    if values[i] + 1 != values[i + 1]:
        print(values[i] + 1)
        break
