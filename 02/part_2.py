
with open('file.in', 'rt') as fin:
    lines = fin.readlines()

parsed_lines = []
no_correct = 0

for line in lines:
    left, text = list(map(lambda x: x.strip(), line.split(':')))
    numbers, letter = left.split(' ')
    first_index, second_index = list(
        map(lambda x: int(x) - 1, numbers.split('-')))

    count = 0

    if text[first_index] == letter:
        count += 1

    if text[second_index] == letter:
        count += 1

    if count == 1:
        no_correct += 1


print(no_correct)
