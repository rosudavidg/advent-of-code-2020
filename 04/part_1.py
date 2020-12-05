import itertools

fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

lines = []

with open('file.in', 'rt') as fin:
    for line in fin.readlines():
        lines.append(line.strip())

current = set()
no_correct = 0
current_is_correct = True

for line in lines:
    if line == '':
        if current_is_correct and len(fields.difference(current)) == 0:
            no_correct += 1

        current = set()
        current_is_correct = True
    else:
        if not current_is_correct:
            continue

        pairs = line.split(' ')

        for pair in pairs:
            key, value = pair.split(':')

            if key != 'cid':
                current.add(key)

            if key == 'byr':
                if len(value) != 4:
                    current_is_correct = False

                if int(value) < 1920 or 2002 < int(value):
                    current_is_correct = False

            if key == 'iyr':
                if len(value) != 4:
                    current_is_correct = False

                if int(value) < 2010 or 2020 < int(value):
                    current_is_correct = False

            if key == 'eyr':
                if len(value) != 4:
                    current_is_correct = False

                if int(value) < 2020 or 2030 < int(value):
                    current_is_correct = False

            if key == 'hgt':
                v = "".join(itertools.takewhile(str.isdigit, value))
                u = value[len(v):]

                if u == 'cm':
                    if int(v) < 150 or 193 < int(v):
                        current_is_correct = False
                elif u == 'in':
                    if int(v) < 59 or 76 < int(v):
                        current_is_correct = False
                else:
                    current_is_correct = False
            if key == 'hcl':
                if len(value) != 7:
                    current_is_correct = False
                    break

                if value[0] != "#":
                    current_is_correct = False
                    break

                for i in range(1):
                    if value[1 + i] not in ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        current_is_correct = False
            if key == 'ecl':
                if value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    current_is_correct = False
            if key == 'pid':
                if len(value) != 9:
                    current_is_correct = False
                else:
                    v = "".join(itertools.takewhile(str.isdigit, value))
                    if v == value:
                        current_is_correct = False


if current_is_correct and len(fields.difference(current)) == 0:
    no_correct += 1

current = set()
current_is_correct = True

current = set()

print(no_correct)
