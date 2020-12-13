with open('file.in', 'rt') as fin:
    timestamp = int(fin.readline())
    busses = list(filter(lambda x: x != None, list(map(lambda x: int(x) if x !=
                                                       'x' else None, fin.readline().split(',')))))

res = []

for bus in busses:
    if timestamp % bus == 0:
        print(bus)
        break
    else:
        res.append((bus - timestamp % bus, bus))

ans = res[0][0] * res[1][1]
minimum = res[0][0]

for time, bus in res:
    if time < minimum:
        ans = time * bus

print(ans)
