number = int(input())


def is_perfect(number):
    sum_divisors = 0
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            sum_divisors += i
    if sum_divisors == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


result = is_perfect(number)
print(result)
