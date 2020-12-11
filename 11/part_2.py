from copy import deepcopy

EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'


def get_occupied_count(i, j, grid):
    count = 0

    for off_x, off_y in [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
        x = off_x
        y = off_y

        occupied = False

        while not occupied:
            if i + x < 0 or j + y < 0 or i + x >= len(grid) or j + y >= len(grid[0]):
                break

            if grid[i + x][j + y] == OCCUPIED:
                count += 1
                occupied = True
                break
            elif grid[i + x][j + y] == EMPTY:
                break
            else:
                x += off_x
                y += off_y

    return count


def next_state(i, j, grid):
    if grid[i][j] == FLOOR:
        return FLOOR

    if grid[i][j] == EMPTY:
        if get_occupied_count(i, j, grid) == 0:
            return OCCUPIED

    if grid[i][j] == OCCUPIED:
        if get_occupied_count(i, j, grid) >= 5:
            return EMPTY

    return grid[i][j]


with open('file.in', 'rt') as fin:
    grid = list(map(lambda l: list(l.strip()), fin.readlines()))

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
