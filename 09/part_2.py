preamble = 25
numbers = []
target = None

# Part 1


def is_valid(no, sums):
    for v in sums.values():
        if no in v:
            return True

    return False


with open('file.in', 'rt') as fin:
    numbers = list(map(int, fin.readlines()))

sums = dict()

for i in range(preamble):
    sums[numbers[i]] = set()

    for j in range(i + 1, preamble):
        sums[numbers[i]].add(numbers[i] + numbers[j])

index = preamble

while True:
    no = numbers[index]

    if not is_valid(no, sums):
        target = no
        break

    del sums[numbers[index - preamble]]

    for k, v in sums.items():
        v.add(no + k)

    sums[no] = set()

    index += 1

# Part 2
dp = [[None for _ in range(len(numbers))] for _ in range(len(numbers))]

for i in range(len(numbers)):
    dp[i][i] = numbers[i]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        dp[i][j] = dp[i][j - 1] + numbers[j]

        if dp[i][j] == target:
            print(min(numbers[i: j + 1]) + max(numbers[i: j + 1]))
            break
