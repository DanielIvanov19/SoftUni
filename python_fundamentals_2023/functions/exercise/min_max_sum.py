numbers_list = [int(num) for num in input().split()]


def min_max_sum(numbers):
    min_num = min(numbers)
    max_num = max(numbers)
    sum_nums = sum(numbers)
    result = [min_num, max_num, sum_nums]
    return result


res_list = min_max_sum(numbers_list)
print(f"The minimum number is {res_list[0]}")
print(f"The maximum number is {res_list[1]}")
print(f"The sum number is: {res_list[2]}")
