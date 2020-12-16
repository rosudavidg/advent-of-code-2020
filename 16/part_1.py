lines = []
ranges = []
my_ticket = ()
nearby_tickets = []

with open('file.in', 'rt') as fin:
    lines = fin.readlines()

i = 0

# Parse ranges
while lines[i] != "\n":
    _, right = lines[i].split(':')
    intervals = right.split('or')

    for interval in intervals:
        left, right = interval.split('-')

        ranges.append((int(left.strip()), int(right.strip())))

    i += 1

# Parse my ticket
i += 2
my_ticket = tuple(map(int, lines[i].strip().split(',')))

# Parse nearby tickets
i += 3
for k in lines[i:]:
    nearby_tickets.append(tuple(map(int, k.strip().split(','))))

res = 0

for ticket in nearby_tickets:

    for value in ticket:
        valid = False

        for range in ranges:
            if value >= range[0] and value <= range[1]:
                valid = True
                break

        if not valid:
            res += value

print(res)
