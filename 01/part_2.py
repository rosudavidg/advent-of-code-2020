target = 2020

with open('file.in', 'rt') as fin:
    numbers = list(map(int, fin.readlines()))

result = None

for i in range(len(numbers) - 2):
    for j in range(i + 1, len(numbers)):
        if (target - numbers[i] - numbers[j]) in numbers[j:]:
            result = (target - numbers[i] - numbers[j]
                      ) * numbers[i] * numbers[j]
            break

print(result)
