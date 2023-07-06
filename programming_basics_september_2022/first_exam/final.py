num_dancers = int(input())
num_points = float(input())
season = input()
place = input()
money = 0
if place == "Bulgaria":
    money = num_points * num_dancers
    if season == "summer":
        money = money * 0.95
    elif season == "winter":
        money = money * 0.92
elif place == "Abroad":
    money = (num_points * num_dancers) * 1.5
    if season == "summer":
        money = money * 0.9
    elif season == "winter":
        money = money * 0.85
charity_sum = money * 0.75
money_per_dancer = (money - charity_sum)/num_dancers
print(f"Charity - {charity_sum:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")