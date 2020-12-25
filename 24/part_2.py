from copy import deepcopy

DIR_NW = 'nw'
DIR_NE = 'ne'
DIR_E = 'e'
DIR_W = 'w'
DIR_SW = 'sw'
DIR_SE = 'se'

DAYS = 100


def normalize(freq):
    updated = True
    while updated == True:
        updated = False

        se_w = min([freq[DIR_SE], freq[DIR_W]])
        freq[DIR_SE] -= se_w
        freq[DIR_W] -= se_w
        freq[DIR_SW] += se_w

        if se_w != 0:
            updated = True

        sw_e = min([freq[DIR_SW], freq[DIR_E]])
        freq[DIR_SW] -= sw_e
        freq[DIR_E] -= sw_e
        freq[DIR_SE] += sw_e

        if sw_e != 0:
            updated = True

        ne_w = min([freq[DIR_NE], freq[DIR_W]])
        freq[DIR_NE] -= ne_w
        freq[DIR_W] -= ne_w
        freq[DIR_NW] += ne_w

        if ne_w != 0:
            updated = True

        nw_e = min([freq[DIR_NW], freq[DIR_E]])
        freq[DIR_NW] -= nw_e
        freq[DIR_E] -= nw_e
        freq[DIR_NE] += nw_e

        if nw_e != 0:
            updated = True

        nw_se = min([freq[DIR_NW], freq[DIR_SE]])
        freq[DIR_NW] -= nw_se
        freq[DIR_SE] -= nw_se

        if nw_se != 0:
            updated = True

        ne_sw = min([freq[DIR_NE], freq[DIR_SW]])
        freq[DIR_NE] -= ne_sw
        freq[DIR_SW] -= ne_sw

        if ne_sw != 0:
            updated = True

        nw_sw = min([freq[DIR_NW], freq[DIR_SW]])
        freq[DIR_NW] -= nw_sw
        freq[DIR_SW] -= nw_sw
        freq[DIR_W] += nw_sw

        if nw_sw != 0:
            updated = True

        ne_se = min([freq[DIR_NE], freq[DIR_SE]])
        freq[DIR_NE] -= ne_se
        freq[DIR_SE] -= ne_se
        freq[DIR_E] += ne_se

        if ne_se != 0:
            updated = True

        e_w = min([freq[DIR_E], freq[DIR_W]])
        freq[DIR_E] -= e_w
        freq[DIR_W] -= e_w

        if e_w != 0:
            updated = True


with open('file.in', 'rt') as fin:
    lines = list(map(lambda line: line.strip(), fin.readlines()))

freqs = []

for line in lines:
    freq = {DIR_NW: 0, DIR_NE: 0, DIR_E: 0, DIR_W: 0, DIR_SW: 0, DIR_SE: 0}
    i = 0

    while i < len(line):
        if line[i] == DIR_E:
            freq[DIR_E] += 1
        elif line[i] == DIR_W:
            freq[DIR_W] += 1
        elif line[i] == 'n':
            i += 1
            if line[i] == 'e':
                freq[DIR_NE] += 1
            elif line[i] == 'w':
                freq[DIR_NW] += 1
        elif line[i] == 's':
            i += 1
            if line[i] == 'e':
                freq[DIR_SE] += 1
            elif line[i] == 'w':
                freq[DIR_SW] += 1

        i += 1

    freqs.append(freq)

for freq in freqs:
    normalize(freq)

tiles = []

for freq in freqs:
    if freq in tiles:
        tiles.remove(freq)
    else:
        tiles.append(freq)

for day in range(DAYS):
    print(day)
    all_neighbours = []
    all_neighbours_blacks = []
    black_to_white = []
    white_to_black = []

    for tile in tiles:
        neighbour_e = deepcopy(tile)
        neighbour_w = deepcopy(tile)
        neighbour_ne = deepcopy(tile)
        neighbour_nw = deepcopy(tile)
        neighbour_sw = deepcopy(tile)
        neighbour_se = deepcopy(tile)

        neighbour_e[DIR_E] += 1
        neighbour_w[DIR_W] += 1
        neighbour_ne[DIR_NE] += 1
        neighbour_nw[DIR_NW] += 1
        neighbour_sw[DIR_SW] += 1
        neighbour_se[DIR_SE] += 1

        normalize(neighbour_e)
        normalize(neighbour_w)
        normalize(neighbour_ne)
        normalize(neighbour_nw)
        normalize(neighbour_sw)
        normalize(neighbour_se)

        neighbours = [neighbour_e, neighbour_w, neighbour_ne,
                      neighbour_nw, neighbour_sw, neighbour_se]

        count = 0

        for neighbour in neighbours:
            if neighbour in all_neighbours:
                all_neighbours_blacks[all_neighbours.index(neighbour)] += 1
            else:
                all_neighbours.append(neighbour)
                all_neighbours_blacks.append(1)

            if neighbour in tiles:
                count += 1

        if count == 0 or count > 2:
            black_to_white.append(tile)

    for i in range(len(all_neighbours)):
        neighbour = all_neighbours[i]
        v = all_neighbours_blacks[i]
        if neighbour not in tiles:
            if v == 2:
                white_to_black.append(neighbour)

    for tile in black_to_white:
        tiles.remove(tile)
    for tile in white_to_black:
        tiles.append(tile)

    print(len(tiles))
