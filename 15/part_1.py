target_position = 2020

with open('file.in', 'rt') as fin:
    in_numbers = list(map(int, fin.readline().split(',')))

numbers = dict()

for i, in_nr in enumerate(in_numbers):
    numbers[in_nr] = i

i = len(in_numbers)
last_number = 0

while i != target_position - 1:
    if last_number in numbers:
        next_number = i - numbers[last_number]
    else:
        next_number = 0

    numbers[last_number] = i

    i += 1
    last_number = next_number

print(last_number)
