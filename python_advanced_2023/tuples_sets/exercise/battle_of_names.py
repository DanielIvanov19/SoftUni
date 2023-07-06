sum_ascii_odd = set()
sum_ascii_even = set()

for row in range(1, int(input()) + 1):
    ascii_sum = sum(ord(l) for l in input()) // row

    # sum_ascii_even.add(ascii_sum) if ascii_sum % 2 == 0 else odd_set.add(ascii_sum) -> shorthand syntax

    if ascii_sum % 2 == 0:
        sum_ascii_even.add(ascii_sum)
    else:
        sum_ascii_odd.add(ascii_sum)

if sum(sum_ascii_odd) > sum(sum_ascii_even):
    print(*sum_ascii_odd.difference(sum_ascii_even), sep=', ')
elif sum(sum_ascii_odd) < sum(sum_ascii_even):
    print(*sum_ascii_odd.symmetric_difference(sum_ascii_even), sep=', ')
else:
    print(*sum_ascii_odd.union(sum_ascii_even), sep=', ')
