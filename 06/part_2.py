lines = []

with open('file.in', 'rt') as fin:
    lines = list(map(lambda l: l.strip(), fin.readlines()))

lines.append('')

res = 0
people = 0
aux = '0' * 26

for line in lines:
    if line == '':
        res += len(list(filter(lambda x: x == people, list(map(int, aux)))))
        aux = '0' * 26
        people = 0
    else:
        people += 1

        for letter in list(line):
            index = ord(letter) - ord('a')
            aux = aux[:index] + str(int(aux[index]) + 1) + aux[index + 1:]

print(res)
