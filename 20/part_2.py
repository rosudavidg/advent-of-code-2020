# Even if this works... don't try to read it :) horriblest solution ever

import math

TRANSFORMATION_1 = 1
TRANSFORMATION_2 = 2
TRANSFORMATION_3 = 3
TRANSFORMATION_4 = 4
TRANSFORMATION_5 = 5
TRANSFORMATION_6 = 6
TRANSFORMATION_7 = 7
TRANSFORMATION_8 = 8

monster = ["                  # ",
           "#    ##    ##    ###",
           " #  #  #  #  #  #   "]

tiles = []


def rotate_90_clock(tile):
    e = list(zip(*tile[::-1]))

    res = []

    for l in e:
        res.append("".join(l))
    return res


def rotate_clock(tile, times):
    for _ in range(times):
        tile = rotate_90_clock(tile)

    return tile


def flip(tile):
    return tile[::-1]


def find_monsters(image, size):
    rotations = 0
    monster_count = 0
    monster_diez = 0

    for line in monster:
        monster_diez += line.count('#')

    while True:
        for i in range(size - len(monster)):
            for j in range(size - len(monster[0])):
                found = True

                for k in range(len(monster)):
                    for l in range(len(monster[0])):
                        if monster[k][l] == '#' and image[i + k][j + l] != '#':
                            found = False
                            l = len(monster[0])
                            k = len(monster)
                            break

                if found == True:
                    monster_count += 1

        if monster_count == 0:
            image = rotate_clock(image, 1)
            rotations += 1

            if rotations == 4:
                image = flip(image)
                rotations = 0
        else:
            break

    total_diez = 0
    for line in image:
        total_diez += line.count('#')
    res = total_diez - monster_diez * monster_count

    return res


def image_from_tiles(new_tiles, graph):
    image = []

    for i in range(len(graph)):
        for j in range(1, 9):
            line = ''

            for k in range(len(graph)):
                line += new_tiles[i][k][j][1:-1]
            image.append(line)

    size = (len(new_tiles[0][0]) - 2) * len(graph)
    return image, size


def flip_tiles(new_tiles, graph):
    for i in range(len(graph)):
        for j in range(len(graph) - 1):
            left = "".join(e[-1] for e in new_tiles[i][j])
            right = "".join(e[0] for e in new_tiles[i][j + 1])

            if left != right:
                if right[::-1] == left:
                    new_tiles[i][j + 1] = flip(new_tiles[i][j + 1])
                else:
                    new_tiles[i][j] = flip(new_tiles[i][j])

    if new_tiles[0][0][-1] != new_tiles[1][0][0]:
        if new_tiles[0][0][0] == new_tiles[1][0][0]:
            i = 0
            for j in range(len(graph)):
                new_tiles[i][j] = flip(new_tiles[i][j])
        elif new_tiles[0][0][-1] == new_tiles[1][0][-1]:
            i = 1
            for j in range(len(graph)):
                new_tiles[i][j] = flip(new_tiles[i][j])
        else:
            i = 0
            for j in range(len(graph)):
                new_tiles[i][j] = flip(new_tiles[i][j])
            i = 1
            for j in range(len(graph)):
                new_tiles[i][j] = flip(new_tiles[i][j])

    for i in range(1, len(graph)):
        if new_tiles[i - 1][0][-1] != new_tiles[i][0][0]:
            for j in range(len(graph)):
                new_tiles[i][j] = flip(new_tiles[i][j])

    return new_tiles


def transform_tiles(tiles, graph, transformations):
    new_tiles = [[None for _ in range(len(graph))] for _ in range(len(graph))]

    for i in range(len(graph)):
        for j in range(len(graph)):

            if j == len(graph) - 1:
                t = transformations[(graph[i][j], graph[i][j - 1])]
                tile = [tile[1] for tile in tiles if tile[0] == graph[i][j]][0]
            else:
                t = transformations[(graph[i][j], graph[i][j + 1])]
                tile = [tile[1] for tile in tiles if tile[0] == graph[i][j]][0]

            if t == TRANSFORMATION_1:
                tile = rotate_90_clock(tile)
            if t == TRANSFORMATION_2:
                tile = flip(rotate_clock(tile, 3))
            if t == TRANSFORMATION_3:
                tile = rotate_clock(flip(tile), 3)
            if t == TRANSFORMATION_4:
                tile = rotate_clock(tile, 3)
            if t == TRANSFORMATION_5:
                tile = rotate_clock(
                    flip(rotate_clock(tile, 1)), 3)
            if t == TRANSFORMATION_6:
                tile = tile
            if t == TRANSFORMATION_7:
                tile = rotate_clock(tile, 2)
            if t == TRANSFORMATION_8:
                tile = flip(tile)

            if j == len(graph) - 1:
                tile = rotate_clock(flip(tile), 2)

            new_tiles[i][j] = tile

    return new_tiles


def get_graph(tiles, nodes, edges):

    corner = []
    for i in range(len(tiles)):
        if nodes.count(tiles[i][0]) == 2:
            corner = tiles[i][0]

    size = int(math.sqrt(len(tiles)))

    graph = [[0 for _ in range(size)] for _ in range(size)]
    graph[0][0] = corner

    graph[0][1] = list(edges[corner])[0]
    graph[1][0] = list(edges[corner])[1]

    edges[corner].remove(graph[0][1])
    edges[corner].remove(graph[1][0])
    edges[graph[0][1]].remove(corner)
    edges[graph[1][0]].remove(corner)

    for diag in range(2, 2 * size - 1):
        start_i = 0 if diag < size else diag - size + 1
        start_j = min([diag, size - 1])

        i = start_i
        j = start_j
        if start_i == 0:
            i = 1
            j -= 1

        while i < size and j > 0:
            up = graph[i - 1][j]
            left = graph[i][j - 1]

            graph[i][j] = list(edges[up].intersection(edges[left]))[0]

            edges[up].remove(graph[i][j])
            edges[left].remove(graph[i][j])
            edges[graph[i][j]].remove(up)
            edges[graph[i][j]].remove(left)

            i += 1
            j -= 1

        up = graph[start_i][start_j - 1]
        if len(edges[up]) > 0:
            graph[start_i][start_j] = list(edges[up])[0]

            edges[up].remove(graph[start_i][start_j])
            edges[graph[start_i][start_j]].remove(up)

        left = graph[i - 1][j]
        if len(edges[left]) > 0:
            graph[i][j] = list(edges[left])[0]

            edges[left].remove(graph[i][j])
            edges[graph[i][j]].remove(left)

    return graph


def get_transformations(tiles):
    for i in range(len(tiles)):
        tile = tiles[i]
        edges = []

        edges.append((tile[1][0], TRANSFORMATION_1))
        edges.append((tile[1][-1], TRANSFORMATION_2))
        edges.append((tile[1][0][::-1], TRANSFORMATION_3))
        edges.append((tile[1][-1][::-1], TRANSFORMATION_4))
        edges.append((''.join([e[0] for e in tile[1]]), TRANSFORMATION_5))
        edges.append((''.join([e[-1] for e in tile[1]]), TRANSFORMATION_6))
        edges.append(
            (''.join([e[0] for e in tile[1]][::-1]), TRANSFORMATION_7))
        edges.append(
            (''.join([e[-1] for e in tile[1][::-1]]), TRANSFORMATION_8))

        tiles[i] = (tiles[i][0], tiles[i][1], edges)

    nodes = []
    edges = {}
    transformations = {}

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

                target = list(set(edges_i).intersection(set(edges_j)))[0]
                t1 = [e[1] for e in tiles[i][2] if e[0] == target][0]
                t2 = [e[1] for e in tiles[j][2] if e[0] == target][0]

                transformations[(tiles[i][0], tiles[j][0])] = t1
                transformations[(tiles[j][0], tiles[i][0])] = t2

    return transformations, nodes, edges


def get_tiles():
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

    return tiles


def main():
    tiles = get_tiles()

    transformations, nodes, edges = get_transformations(tiles)

    graph = get_graph(tiles, nodes, edges)

    tiles = transform_tiles(tiles, graph, transformations)

    tiles = flip_tiles(tiles, graph)

    image, size = image_from_tiles(tiles, graph)

    res = find_monsters(image, size)

    print(res)


if __name__ == '__main__':
    main()
