with open('file.in', 'rt') as fin:
    numbers = list(map(int, fin.readlines()))

numbers.sort()
differences = {0: 0, 1: 0, 2: 0, 3: 1}

for i in range(len(numbers) - 1):
    differences[numbers[i + 1] - numbers[i]] += 1


differences[numbers[0]] += 1
print(differences[1])
print(differences[3])
print(differences[1] * differences[3])
