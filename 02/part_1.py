
with open('file.in', 'rt') as fin:
    lines = fin.readlines()

parsed_lines = []
no_correct = 0

for line in lines:
    left, text = line.split(':')
    numbers, letter = left.split(' ')
    minimum, maximum = list(map(int, numbers.split('-')))

    count = text.count(letter)

    if minimum <= count and count <= maximum:
        no_correct += 1

print(no_correct)
