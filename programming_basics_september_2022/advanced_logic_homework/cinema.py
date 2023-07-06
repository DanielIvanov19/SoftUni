premiere = 12
normal = 7.5
discount = 5

screening_type = input()
rows = int(input())
columns = int(input())

income = 0

if screening_type == "Premiere":
    income = premiere * rows * columns
elif screening_type == "Normal":
    income = normal * rows * columns
elif screening_type == "Discount":
    income = discount * rows * columns

print(f"{income:.2f} leva")