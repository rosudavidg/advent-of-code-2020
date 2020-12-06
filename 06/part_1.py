lines = []

with open('file.in', 'rt') as fin:
    lines = list(map(lambda l: l.strip(), fin.readlines()))

lines.append('')

res = 0
aux = '0' * 26

for line in lines:
    if line == '':
        res += aux.count('1')
        aux = '0' * 26
    else:
        for letter in list(line):
            index = ord(letter) - ord('a')
            aux = aux[:index] + '1' + aux[index + 1:]

print(res)
