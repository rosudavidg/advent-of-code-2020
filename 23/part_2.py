from utils import CreateList

ROUNDS = 10000000
CUP_COUNT = 1000000
MAX_VALUE = 1000000

with open('file.in', 'rt') as fin:
    cups = list(map(int, list(fin.readline())))

while len(cups) != CUP_COUNT:
    cups.append(len(cups) + 1)


indexes = dict()
cup_list = CreateList()
for cup in cups:
    cup_list.add(cup)
    indexes[cup] = cup_list.tail

current_cup = cup_list.head

for _ in range(ROUNDS):
    group_start = current_cup.next
    group_end = group_start.next.next

    group = [group_start.data, group_start.next.data,
             group_start.next.next.data]

    next_value = current_cup.data - 1

    if next_value == 0:
        next_value = MAX_VALUE

    while (next_value in group) or (next_value not in indexes):
        next_value -= 1

        if next_value == 0:
            next_value = MAX_VALUE

    next = indexes[next_value]

    current_cup.next = group_end.next
    group_end.next = next.next
    next.next = group_start

    current_cup = current_cup.next

print(indexes[1].next.data * indexes[1].next.next.data)
