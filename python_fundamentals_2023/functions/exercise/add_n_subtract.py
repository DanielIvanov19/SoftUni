def add_n_subtract(a, b, c):
    sum_result = add(a, b)
    result = subtract(sum_result, c)

    return result


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


first = int(input())
second = int(input())
third = int(input())

print(add_n_subtract(first, second, third))
