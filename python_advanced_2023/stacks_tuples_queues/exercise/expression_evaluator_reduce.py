from collections import deque
import math
from functools import reduce
expression = input().split()
index = 0

functions = {
    '*': lambda i: reduce(lambda a, b: a*b, map(int, expression[:i])),
    '*': lambda i: reduce(lambda a, b: a/b, map(int, expression[:i])),
    '*': lambda i: reduce(lambda a, b: a+b, map(int, expression[:i])),
    '*': lambda i: reduce(lambda a, b: a-b, map(int, expression[:i]))
}

while index < len(expression):
    element = expression[index]

    if element in '*/+-':
        expression[0] = functions[element](index)
        [expression.pop(1) for i in range(index)]
        index = 1
    index += 1
print(math.floor(int(expression[0])))
