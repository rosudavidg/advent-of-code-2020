preamble = 25
numbers = []


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
        print(no)
        break

    del sums[numbers[index - preamble]]

    for k, v in sums.items():
        v.add(no + k)

    sums[no] = set()

    index += 1
