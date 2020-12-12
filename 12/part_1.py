from copy import deepcopy

NORTH = 'N'
SOUTH = 'S'
EAST = 'E'
WEST = 'W'
LEFT = 'L'
RIGHT = 'R'
FORWARD = 'F'

offsets = {NORTH: (0, -1), SOUTH: (0, 1), EAST: (1, 0), WEST: (-1, 0)}
offsets_degrees = {EAST: 0, SOUTH: 90, WEST: 180, NORTH: 270}

facing = EAST
position = (0, 0)


def turn(facing, direction, degrees):
    rot = offsets_degrees[facing]

    if direction == RIGHT:
        rot += degrees
    else:
        rot += 360 - degrees

    rot = rot % 360

    for k, v in offsets_degrees.items():
        if v == rot:
            return k


with open('file.in', 'rt') as fin:
    moves = list(
        map(lambda l: (l[0], int(l[1:])), fin.readlines()))


for move in moves:
    action = move[0]
    value = move[1]

    if action in [NORTH, SOUTH, EAST, WEST]:
        position = (position[0] + value * offsets[action]
                    [0], position[1] + value * offsets[action][1])
    elif action in [LEFT, RIGHT]:
        facing = turn(facing, action, value)
    else:
        position = (position[0] + value * offsets[facing]
                    [0], position[1] + value * offsets[facing][1])

print(sum(list(map(abs, position))))
