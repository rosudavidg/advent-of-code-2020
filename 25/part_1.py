import itertools

with open('file.in', 'rt') as fin:
    pk_card, pk_door = list(map(int, fin.readlines()))

loop_card = 0
aux = 1
while True:
    loop_card += 1

    if pow(7, loop_card, 20201227) == pk_card:
        break

print(pow(pk_door, loop_card, 20201227))
