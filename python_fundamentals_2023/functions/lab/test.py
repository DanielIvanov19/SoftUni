def multiply_numbers(n_1, n_2):
    result = n_1 * n_2
    return result


print(multiply_numbers(5, 10))

nums_as_strings = ["1", "2", "3"]
nums = map(int, nums_as_strings)
for num in nums:
    print(num)
# in this variant the nums disappear
nums_2 = list(map(int, nums_as_strings))
# in this variant a list of integers is created
nums_3 = [int(el) for el in nums_as_strings]
# in this variant a list of integers is created
nums_4 = list(filter(lambda x: x% 2 == 0, nums_as_strings))
# filters the even numbers and makes a list of them
# we use lambda if we want to use a function once
