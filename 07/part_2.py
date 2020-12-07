lines = []
rules = dict()


def bags(bag):
    res = 0

    for count, color in rules[bag]:
        res += count + count * bags(color)

    return res


with open('file.in', 'rt') as fin:
    lines = list(map(lambda l: l.strip(), fin.readlines()))


for line in lines:
    left, right = line.split('contain')

    outter = ' '.join(left.strip().split(' ')[:-1])
    inners = list(filter(lambda e: e != None, list(map(lambda bag_raw: (int(bag_raw.strip().split(' ')[0]), ' '.join(bag_raw.strip().split(' ')[1:-1])) if bag_raw.split(' ')[0] != 'no' else None,
                                                       right.strip().split(',')))))

    rules[outter] = inners

print(bags('shiny gold'))
