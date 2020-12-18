# NOTE: ugliest solution ever :) I will come back to use binary trees

from copy import deepcopy
ADD = '+'
MUL = '*'
LPAREN = '('
RPAREN = ')'


def order_add(expression):
    if not isinstance(expression, list):
        return expression

    parsed_elements = []
    for element in expression:
        parsed_elements.append(order_add(element))

    expression = parsed_elements

    parsed_expression = []
    i = 0
    while i < len(expression):
        if expression[i] == ADD:
            left = parsed_expression[-1]
            right = expression[i + 1]

            parsed_expression[-1] = [left, ADD, right]

            i += 2
        else:
            parsed_expression.append(expression[i])
            i += 1

    expression = parsed_expression

    return expression


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


parsed_expressions = []
for expression in expressions:
    parsed_expressions.append(order_add(expression))

expressions = parsed_expressions

res = 0
for expression in expressions:
    res += evaluate(expression)

print(res)
