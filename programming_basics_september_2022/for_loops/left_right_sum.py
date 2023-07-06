n = int(input())
sum_left = 0
sum_right = 0
for i in range(1, n * 2 + 1):
    num = int(input())
    if i <= n:
        sum_left += num
    else:
        sum_right += num
diff = abs(sum_left - sum_right)
if sum_left == sum_right:
    print(f"Yes, sum = {sum_left}")
else:
    print(f"No diff = {diff}")