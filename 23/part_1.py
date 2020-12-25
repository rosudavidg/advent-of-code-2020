ROUNDS = 100
GROUP_SIZE = 3

with open('file.in', 'rt') as fin:
    cups = list(map(int, list(fin.readline())))

current_pos = 0
current_cup = cups[current_pos]

for round in range(ROUNDS):
    group = cups[current_pos + 1: current_pos + 1 + GROUP_SIZE] + cups[: GROUP_SIZE -
                                                                       (len(cups) - current_pos) + 1 if (len(cups) - current_pos) <= GROUP_SIZE else 0]

    for cup in group:
        cups.remove(cup)

    group_less = [e for e in cups if e < current_cup]

    if len(group_less) == 0:
        pivot = max(cups)
    else:
        pivot = max(group_less)

    pivot_pos = cups.index(pivot)

    cups = cups[:pivot_pos + 1] + group + cups[pivot_pos + 1:]
    current_pos = cups.index(current_cup) + 1
    if current_pos >= len(cups):
        current_pos = 0
    current_cup = cups[current_pos]

pivot = cups.index(1)

print(''.join(list(map(str, cups[pivot + 1:] + cups[:pivot]))))
