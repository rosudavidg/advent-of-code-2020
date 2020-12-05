
lines = []

right = 3
down = 1
global_count = 1

with open('file.in', 'rt') as fin:
    for line in fin.readlines():
        lines.append(list(line.strip()))

for (right, down) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    tree_count = 0
    i = down
    j = right

    while i < len(lines):
        if lines[i][j % len(lines[0])] == '#':
            tree_count += 1

        i += down
        j += right

    if tree_count != 0:
        global_count *= tree_count

print(global_count)
