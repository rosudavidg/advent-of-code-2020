DIR_NW = 'nw'
DIR_NE = 'ne'
DIR_E = 'e'
DIR_W = 'w'
DIR_SW = 'sw'
DIR_SE = 'se'

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


tiles = []
for freq in freqs:
    tiles.append(
        f'{freq[DIR_W]}-{freq[DIR_E]}-{freq[DIR_NW]}-{freq[DIR_SE]}-{freq[DIR_SW]}-{freq[DIR_NE]}')

colors = dict()
for tile in tiles:
    if tile in colors:
        colors[tile] *= (-1)
    else:
        colors[tile] = 1

for k, v in colors.items():
    print(k, v)


res = 0
for k, v in colors.items():
    if v == 1:
        res += 1

print(res)
