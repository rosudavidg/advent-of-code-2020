
lines = []

right = 3
down = 1

with open('file.in', 'rt') as fin:
    for line in fin.readlines():
        lines.append(list(line.strip()))

tree_count = 0
i = down
j = right

while i < len(lines):
    if lines[i][j % len(lines[0])] == '#':
        tree_count += 1

    i += down
    j += right

print(tree_count)
