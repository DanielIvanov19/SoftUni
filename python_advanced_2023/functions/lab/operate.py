from functools import reduce


def operate(operator, *args):
    if operator == '+':
        return reduce(lambda a, b: a + b, args)
    elif operator == '-':
        return reduce(lambda a, b: a + b, args)
    elif operator == '*':
        return reduce(lambda a, b: a + b, args)
    else:
        return reduce(lambda a, b: a + b, args)

    # return reduce(lambda a, b: eval(f'{a}{operator}{b}'), args) -> what is in the string evaluates as a number

print(operate('+', 2, 3))
