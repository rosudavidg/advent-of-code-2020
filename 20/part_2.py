import math

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
edges = {}
size = int(math.sqrt(len(tiles)))

for i in range(len(tiles)):
    edges[tiles[i][0]] = set()

for i in range(len(tiles) - 1):
    for j in range(i + 1, len(tiles)):
        edges_i = [e[0] for e in tiles[i][2]]
        edges_j = [e[0] for e in tiles[j][2]]

        if len(set(edges_i).intersection(set(edges_j))) != 0:
            nodes.append(tiles[i][0])
            nodes.append(tiles[j][0])
            edges[tiles[i][0]].add(tiles[j][0])
            edges[tiles[j][0]].add(tiles[i][0])

corner = []
for i in range(len(tiles)):
    if nodes.count(tiles[i][0]) == 2:
        corner = tiles[i][0]

graph = [[0 for _ in range(size)] for _ in range(size)]
graph[0][0] = corner

graph[0][1] = list(edges[corner])[0]
graph[1][0] = list(edges[corner])[1]

edges[corner].remove(graph[0][1])
edges[corner].remove(graph[1][0])
edges[graph[0][1]].remove(corner)
edges[graph[1][0]].remove(corner)

print(edges)

for diag in range(2, 2 * size - 1):
    start_i = 0 if diag < size else diag - size + 1
    start_j = min([diag, size - 1])
    print()
    print(start_i, start_j)

    i = start_i
    j = start_j
    if start_i == 0:
        i = 1
        j -= 1
    elif start_j == size - 1:
        i += 1
        j -= 1

    while i < size and j > 0:
        print(i, j)
        up = graph[i - 1][j]
        left = graph[i][j - 1]

        if graph[i][j] != 0:
            i += 1
            j -= 1
            continue

        print(up, left)
        graph[i][j] = list(edges[up].intersection(edges[left]))[0]
        print(graph[i][j])

        edges[up].remove(graph[i][j])
        print(f'sterg din {up} pe {graph[i][j]}')
        edges[left].remove(graph[i][j])
        print(f'sterg din {left} pe {graph[i][j]}')
        edges[graph[i][j]].remove(up)
        print(f'sterg din {graph[i][j]} pe {up}')
        edges[graph[i][j]].remove(left)
        print(f'sterg din {graph[i][j]} pe {left}')

        if len(edges[up]) > 0:
            graph[i - 1][j + 1] = list(edges[up])[0]

            edges[up].remove(graph[i - 1][j + 1])
            print(f'sterg din {up} pe {graph[i - 1][j + 1]}')

            edges[graph[i - 1][j + 1]].remove(up)
            print(f'sterg din {graph[i - 1][j + 1]} pe {up}')

        if len(edges[left]) > 0:
            graph[i + 1][j - 1] = list(edges[left])[0]

            edges[left].remove(graph[i + 1][j - 1])
            print(f'sterg din {left} pe {graph[i + 1][j - 1]}')

            edges[graph[i + 1][j - 1]].remove(left)
            print(f'sterg din {graph[i + 1][j - 1]} pe {left}')

        i += 1
        j -= 1

# graph[size - 1][size - 1] = list(edges[graph[size - 2][size - 1]
#                                        ].intersection(edges[graph[size - 1][size - 2]]))[0]
# edges[graph[size - 2][size - 1]].remove(graph[size - 1][size - 1])
# edges[graph[size - 1][size - 2]].remove(graph[size - 1][size - 1])
# edges[graph[size - 1][size - 1]].remove(graph[size - 2][size - 1])
# edges[graph[size - 1][size - 1]].remove(graph[size - 1][size - 2])

print(graph)
print(edges)
