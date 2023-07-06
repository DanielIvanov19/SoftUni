n = int(input())

b_1 = 0
b_2 = 0
b_3 = 0
b_4 = 0
b_5 = 0
for i in range(1, n + 1):
    current_num = int(input())
    if current_num < 200:
        b_1 += 1
    elif current_num <= 399:
        b_2 += 1
    elif current_num <= 599:
        b_3 += 1
    elif current_num <= 799:
        b_4 += 1
    elif current_num >= 800:
        b_5 += 1
per_1 = b_1 / n * 100
per_2 = b_2 / n * 100
per_3 = b_3 / n * 100
per_4 = b_4 / n * 100
per_5 = b_5 / n * 100
print(f"{per_1:.2f}%")
print(f"{per_2:.2f}%")
print(f"{per_3:.2f}%")
print(f"{per_4:.2f}%")
print(f"{per_5:.2f}%")