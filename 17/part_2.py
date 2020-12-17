from copy import deepcopy

ACTIVE = '#'
INACTIVE = '.'
ROUNDS = 6


def next_state(cubes, x, y, z, w):
    count = 0
    for w_off in range(-1, 2):
        for z_off in range(-1, 2):
            for x_off in range(-1, 2):
                for y_off in range(-1, 2):
                    if cubes[w + w_off][z + z_off][x + x_off][y + y_off] == ACTIVE:
                        count += 1

    if cubes[w][z][x][y] == ACTIVE:
        count -= 1

    if cubes[w][z][x][y] == ACTIVE:
        if count in [2, 3]:
            return ACTIVE
    else:
        if count == 3:
            return ACTIVE

    return INACTIVE


    # Read input
with open('file.in', 'rt') as fin:
    lines = list(map(lambda line: line.strip(), fin.readlines()))

x_size = len(lines) + 2 * ROUNDS + 2
y_size = len(lines[0]) + 2 * ROUNDS + 2
z_size = 1 + 2 * ROUNDS + 2
w_size = 1 + 2 * ROUNDS + 2

# Init cubes [w][z][x][y]
cubes = [[[[INACTIVE for _ in range(y_size)]
           for _ in range(x_size)] for _ in range(z_size)] for _ in range(w_size)]


w = int(w_size / 2)
z = int(z_size / 2)
for x in range(len(lines)):
    for y in range(len(lines[0])):
        cubes[w][z][x + ROUNDS + 1][y + ROUNDS + 1] = lines[x][y]

# Compute rounds
for _ in range(ROUNDS):
    new_cubes = deepcopy(cubes)

    for w in range(1, w_size - 1):
        for z in range(1, z_size - 1):
            for x in range(1, x_size - 1):
                for y in range(1, y_size - 1):
                    new_cubes[w][z][x][y] = next_state(cubes, x, y, z, w)

    cubes = new_cubes

# Compute res
res = 0
for w in range(1, w_size - 1):
    for z in range(1, z_size - 1):
        for x in range(1, x_size - 1):
            for y in range(1, y_size - 1):
                if cubes[w][z][x][y] == '#':
                    res += 1

print(res)
