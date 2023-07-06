numbers_list = [int(num) for num in input().split()]


def sort_numbers(numbers):
    result = sorted(numbers)
    return result


print(sort_numbers(numbers_list))
