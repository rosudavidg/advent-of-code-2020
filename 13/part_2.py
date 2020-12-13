# https://en.wikipedia.org/wiki/Chinese_remainder_theorem
from sympy.ntheory.modular import crt

with open('file.in', 'rt') as fin:
    _ = fin.readline()
    busses = list(map(lambda x: int(x) if x !=
                      'x' else None, fin.readline().split(',')))

mods = []
values = []

for i in range(len(busses)):
    if busses[i] != None:
        mods.append(busses[i] - i)
        values.append(busses[i])

print(crt(values, mods)[0])
