with open('file.in', 'rt') as fin:
    numbers = list(map(int, fin.readlines()))

numbers.sort()

solutions = dict()
for number in numbers:
    solutions[number] = 0
solutions[0] = 1

for number in numbers:
    for prev in range(number - 3, number):
        if prev in solutions:
            solutions[number] += solutions[prev]

print(solutions[numbers[-1]])
