lines = []
ranges = []
my_ticket = ()
nearby_tickets = []
valid_tickets = []

with open('file.in', 'rt') as fin:
    lines = fin.readlines()

i = 0

# Parse ranges
while lines[i] != "\n":
    _, right = lines[i].split(':')
    intervals = right.split('or')

    r = []

    for interval in intervals:
        left, right = interval.split('-')

        r.append((int(left.strip()), int(right.strip())))

    ranges.append(r)

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
    ticket_valid = True

    for value in ticket:
        valid = False

        for r in ranges:
            for rangee in r:
                if value >= rangee[0] and value <= rangee[1]:
                    valid = True
                    break

        if not valid:
            ticket_valid = False
            break

    if ticket_valid:
        valid_tickets.append(ticket)

possibles = [set(list([i for i in range(len(ranges))]))
             for _ in range(len(ranges))]

for ticket in valid_tickets:
    for i in range(len(ticket)):
        possibles_current = set()
        value = ticket[i]

        for j in range(len(ranges)):
            r = ranges[j]
            valid = False

            for rangee in r:
                if value >= rangee[0] and value <= rangee[1]:
                    valid = True

            if valid:
                possibles_current.add(j)

        possibles[i] = possibles[i].intersection(possibles_current)

count = 0
solution = dict()

while count != len(ranges):
    for i, possible in enumerate(possibles):
        if len(possible) == 1:
            value = possible
            solution[i] = list(value)[0]
            count += 1
            break

    possibles = list(map(lambda x: x - set(value
                                           ), possibles))

res = 1
for k, v in solution.items():
    if v in range(6):
        res *= my_ticket[k]
        print(my_ticket[k])

print(res)
