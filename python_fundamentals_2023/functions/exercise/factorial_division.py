first_num = int(input())
second_num = int(input())


def factorial_division(num1, num2):
    factorial_first = 1
    factorial_second = 1
    for i in range(num1, 0, -1):
        factorial_first = factorial_first * i
    for y in range(num2, 0, -1):
        factorial_second = factorial_second * y
    factorials_divided = factorial_first / factorial_second
    return f"{factorials_divided:.2f}"


result = factorial_division(first_num, second_num)
print(result)
