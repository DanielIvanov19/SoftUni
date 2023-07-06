def print_nums(positive_nums, negative_nums):
    print(negative_nums)
    print(positive_nums)

    if positive_nums > abs(negative_nums):
        print('The positives are stronger than the negatives')
    else:
        print('The negatives are stronger than the positives')


numbers = [int(x) for x in input().split()]

positives = sum(x for x in numbers if x > 0)
negatives = sum(x for x in numbers if x < 0)
print_nums(positives, negatives)