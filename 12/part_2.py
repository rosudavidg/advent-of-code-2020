from copy import deepcopy

NORTH = 'N'
SOUTH = 'S'
EAST = 'E'
WEST = 'W'
LEFT = 'L'
RIGHT = 'R'
FORWARD = 'F'

offsets = {NORTH: (0, -1), SOUTH: (0, 1), EAST: (1, 0), WEST: (-1, 0)}
offsets_degrees = {0: (lambda p: (p[0], p[1])), 90: (lambda p: (
    -p[1], p[0])), 180: (lambda p: (-p[0], -p[1])), 270: (lambda p: (p[1], -p[0]))}

position = (0, 0)
waypoint = (10, -1)


def turn(waypoint, direction, degrees):
    if direction == LEFT:
        degrees = 360 - degrees

    degrees = degrees % 360

    return offsets_degrees[degrees](waypoint)


with open('file.in', 'rt') as fin:
    moves = list(
        map(lambda l: (l[0], int(l[1:])), fin.readlines()))


for move in moves:
    action = move[0]
    value = move[1]

    if action in [NORTH, SOUTH, EAST, WEST]:
        waypoint = (waypoint[0] + value * offsets[action]
                    [0], waypoint[1] + value * offsets[action][1])
    elif action in [LEFT, RIGHT]:
        waypoint = turn(waypoint, action, value)
    else:
        position = (position[0] + value * waypoint[0],
                    position[1] + value * waypoint[1])

print(sum(list(map(abs, position))))
