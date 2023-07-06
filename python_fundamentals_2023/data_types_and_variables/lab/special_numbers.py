n = int(input())
# for i in range(1, n + 1):
#    sum_of_digits = 0
#    num = i
#    while num:
#        sum_of_digits += num % 10
#        num = int(num / 10) #could also be num // 10
#    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
#        print(f"{i} -> True")
#    else:
#        print(f"{i} -> False")

is_special = False
for num in range(1, n + 1):
    num_to_str = str(num)
    sum_digits = 0
    for i in num_to_str:
        sum_digits += int(i)
    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        print(f"{num} is special")
    else:
        print(f"{num}")
