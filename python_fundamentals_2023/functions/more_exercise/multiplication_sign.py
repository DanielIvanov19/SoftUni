first_num = int(input())
second_num = int(input())
third_num = int(input())


def multiplication_sign(first, second, third):
    neg_count = 0
    pos_count = 0

    if first == 0 or second == 0 or third == 0:
        return 'zero'

    if first < 0:
        neg_count += 1
    if second < 0:
        neg_count += 1
    if third < 0:
        neg_count += 1
    if first > 0:
        pos_count += 1
    if second > 0:
        pos_count += 1
    if third > 0:
        pos_count += 1

    if neg_count == 1 or neg_count == 3:
        return 'negative'
    else:
        return 'positive'


result = multiplication_sign(first_num, second_num, third_num)
print(result)
