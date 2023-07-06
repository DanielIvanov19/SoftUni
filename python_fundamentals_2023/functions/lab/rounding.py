numbers_list = [float(x) for x in input().split(" ")]


def round_numbers(numbers = [1.2, 2.3]):
    for i in range(len(numbers)):
        numbers[i] = numbers[i].__round__()
    return numbers


print(round_numbers(numbers_list))