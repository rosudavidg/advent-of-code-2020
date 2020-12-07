lines = []

with open('file.in', 'rt') as fin:
    lines = list(map(lambda l: l.strip(), fin.readlines()))

rules = dict()

for line in lines:
    left, right = line.split('contain')

    outter = ' '.join(left.strip().split(' ')[:-1])
    inners = list(filter(lambda e: e != None, list(map(lambda bag_raw: ' '.join(bag_raw.strip().split(' ')[1:-1]) if bag_raw.split(' ')[0] != 'no' else None,
                                                       right.strip().split(',')))))

    for inner in inners:
        if inner in rules:
            rules[inner] = rules[inner].union(set([outter]))
        else:
            rules[inner] = set([outter])


options = set()
queue = ['shiny gold']

while queue:
    e = queue.pop()

    if e not in rules:
        continue

    for option in rules[e]:
        options.add(option)
        queue.append(option)

print(len(options))
