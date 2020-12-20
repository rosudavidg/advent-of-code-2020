LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

tiles = []

with open('file.in', 'rt') as fin:
    lines = list(map(lambda line: line.strip(), fin.readlines()))

i = 0
while i < len(lines):
    tile_id = int(lines[i].split(' ')[1][:-1])
    image = []

    i += 1

    while i < len(lines) and lines[i] != '':
        image.append(lines[i])
        i += 1

    tiles.append((tile_id, image))

    i += 1

for i in range(len(tiles)):
    tile = tiles[i]
    edges = []

    edges.append((tile[1][0], UP))
    edges.append((tile[1][-1], DOWN))
    edges.append((tile[1][0][::-1], UP))
    edges.append((tile[1][-1][::-1], DOWN))
    edges.append((''.join([e[0] for e in tile[1]]), LEFT))
    edges.append((''.join([e[-1] for e in tile[1]]), RIGHT))
    edges.append((''.join([e[0] for e in tile[1]][::-1]), LEFT))
    edges.append((''.join([e[-1] for e in tile[1][::-1]]), RIGHT))

    tiles[i] = (tiles[i][0], tiles[i][1], edges)

nodes = []
for i in range(len(tiles) - 1):
    for j in range(i + 1, len(tiles)):
        edges_i = [e[0] for e in tiles[i][2]]
        edges_j = [e[0] for e in tiles[j][2]]

        if len(set(edges_i).intersection(set(edges_j))) != 0:
            nodes.append(tiles[i][0])
            nodes.append(tiles[j][0])

res = 1
for i in range(len(tiles)):
    if nodes.count(tiles[i][0]) == 2:
        res *= tiles[i][0]

print(res)
