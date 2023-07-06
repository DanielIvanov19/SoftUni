number = input()


def odd_n_even_sum(number):
    number_length = len(number)
    sum_even = 0
    sum_odd = 0
    for num in number:
        if int(num) % 2 == 0:
            sum_even += int(num)
        else:
            sum_odd += int(num)
    return [sum_odd, sum_even]


result = odd_n_even_sum(number)
print(f"Odd sum = {result[0]}, Even sum = {result[1]}")
