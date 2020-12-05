target = 2020

with open('file.in', 'rt') as fin:
    numbers = list(map(int, fin.readlines()))

result = None

for i in range(len(numbers)):
    if (target - numbers[i]) in numbers[i:]:
        result = (target - numbers[i]) * numbers[i]
        break

print(result)
