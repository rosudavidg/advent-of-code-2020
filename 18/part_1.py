# NOTE: ugliest solution ever :) I will come back to use binary trees

ADD = '+'
MUL = '*'
LPAREN = '('
RPAREN = ')'


def evaluate(expression):
    if not isinstance(expression, list):
        return expression

    left = evaluate(expression[0])
    i = 1

    while i != len(expression):
        op = expression[i]
        right = evaluate(expression[i + 1])

        if op == MUL:
            left *= right
        elif op == ADD:
            left += right
        i += 2

    return left


with open('file.in', 'rt') as fin:
    lines = list(map(lambda line: line.strip(), fin.readlines()))

expressions = []
for line in lines:
    elements = []
    stack = []

    for e in line.split(' '):
        if e[0] == LPAREN:
            i = 0
            while e[i] == LPAREN:
                elements.append(e[i])
                i += 1

            elements.append(int(e[i:]))

        elif e[len(e) - 1] == RPAREN:
            i = len(e) - 1
            rparens = []
            while e[i] == RPAREN:
                rparens.append(e[i])
                i -= 1

            elements.append(int(e[:i + 1]))
            elements += rparens

        elif e in [MUL, ADD]:
            elements.append(e)
        else:
            elements.append(int(e))

    expressions.append(elements)

parsed_expressions = []
for expression in expressions:
    elements = []
    stack = []

    for e in expression:
        if e == LPAREN:
            stack.append(elements)
            elements = []
        elif e == RPAREN:
            old_elements = stack.pop(len(stack) - 1)
            old_elements.append(elements)
            elements = old_elements
        else:
            elements.append(e)

    parsed_expressions.append(elements)

expressions = parsed_expressions

res = 0
for expression in expressions:
    res += evaluate(expression)

print(res)
