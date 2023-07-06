import sys
n = int(input())
max_num = -sys.maxsize
suma = 0
for i in range(1, n + 1):
    current_num = int(input())
    if current_num > max_num:
        max_num = current_num
    suma += current_num
other_sum = suma - max_num
if max_num == other_sum:
    print("Yes")
    print(f"Sum = {other_sum}")
else:
    print("No")
    print(f"Diff = {abs(other_sum - max_num)}")
