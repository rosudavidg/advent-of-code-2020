from copy import deepcopy

EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'


def next_state(i, j, grid):
    if grid[i][j] == FLOOR:
        return FLOOR

    if grid[i][j] == EMPTY:
        if grid[i - 1][j - 1] != OCCUPIED and grid[i][j - 1] != OCCUPIED and grid[i + 1][j - 1] != OCCUPIED and grid[i - 1][j] != OCCUPIED and grid[i + 1][j] != OCCUPIED and grid[i - 1][j + 1] != OCCUPIED and grid[i][j + 1] != OCCUPIED and grid[i + 1][j + 1] != OCCUPIED:
            return OCCUPIED

    if grid[i][j] == OCCUPIED:
        count = 0
        for x, y in [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
            if grid[i + x][j + y] == OCCUPIED:
                count += 1
                if count >= 4:
                    return EMPTY

    return grid[i][j]


with open('file.in', 'rt') as fin:
    grid = list(map(lambda l: list(l.strip()), fin.readlines()))

for i in range(len(grid)):
    grid[i] = ['.'] + grid[i] + ['.']

grid.insert(0, list('.' * len(grid[0])))
grid.append(list('.' * len(grid[0])))

while True:
    modified = False

    next_grid = deepcopy(grid)

    for i in range(len(next_grid)):
        for j in range(len(next_grid[i])):
            next_grid[i][j] = next_state(i, j, grid)

            if next_grid[i][j] != grid[i][j]:
                modified = True

    grid = next_grid

    if not modified:
        break

count = 0
for i in range(len(grid)):
    count += ".".join(grid[i]).count(OCCUPIED)

print(count)
