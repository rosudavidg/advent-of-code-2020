rules = {}
matches = {}
solved = set()
tests = []

with open('file.in', 'rt') as fin:
    lines = list(map(lambda line: line.strip(), fin.readlines()))

# Parse data
top = True
for line in lines:
    if line == '':
        top = False
        continue

    if top:
        left, right = line.split(':')

        if "\"" in right:
            matches[int(left)] = [right[2:3]]
            solved.add(int(left))
        else:
            next_rules = []
            needed = set()
            for next_rule in right.split('|'):
                rule = list(map(int, next_rule.strip().split(' ')))
                needed = needed.union(rule)
                next_rules.append(rule)

            rules[int(left)] = (needed, next_rules)

    else:
        tests.append(line)


def solve(k, v):
    _, next_rules = v
    sol = []
    for next_rule in next_rules:
        solutions = ['']

        for i in next_rule:
            next_solutions = []

            for l in solutions:
                for r in matches[i]:
                    next_solutions.append(l + r)

            solutions = next_solutions
        sol += solutions

    matches[k] = sol
    del rules[k]
    solved.add(k)


while len(rules) != 0:
    for k, v in rules.items():
        if len(v[0].difference(solved)) == 0:
            solve(k, v)
            break


max_len = max(list(map(len, tests)))


def func_is_42(s):
    if len(s) == 0:
        return True

    return True in [func_is_42(s[len(k):]) for k in matches[42] if s[:len(k)] == k]


def is_8_11(s):
    is_42 = False
    for k in matches[42]:
        if len(s) >= len(k) and s[:len(k)] == k:
            s = s[len(k):]
            is_42 = True
            break
    if not is_42:
        return False

    is_42 = False
    for k in matches[42]:
        if len(s) >= len(k) and s[:len(k)] == k:
            s = s[len(k):]
            is_42 = True
            break
    if not is_42:
        return False

    is_31 = False
    for k in matches[31]:
        if len(s) >= len(k) and s[-len(k):] == k:
            s = s[:-len(k)]
            is_31 = True
            break
    if not is_31:
        return False

    while True:
        if len(s) == 0:
            return True

        is_42 = False
        for k in matches[42]:
            if len(s) >= len(k) and s[:len(k)] == k:
                s = s[len(k):]
                is_42 = True
                break
        if not is_42:
            return False

        is_31 = False
        for k in matches[31]:
            if len(s) >= len(k) and s[-len(k):] == k:
                s = s[:-len(k)]
                is_31 = True
                break

        if not is_31:
            return func_is_42(s)


res = 0

for test in tests:
    if test in matches[0]:
        res += 1
    elif is_8_11(test):
        res += 1

print(res)
