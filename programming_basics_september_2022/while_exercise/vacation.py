needed_money = float(input())
init_money = float(input())
total_sum = init_money
c_total_days = 0
c_spend_days = 0

while total_sum < needed_money:
    if c_spend_days == 5:
        break
    action = input()
    amount = float(input())
    c_total_days += 1

    if action == "spend":
        c_spend_days += 1
        total_sum -= amount
        if total_sum < 0:
            total_sum = 0
    elif action == "save":
        c_spend_days = 0
        total_sum += amount

if c_spend_days == 5:
    print("You can't save the money")
    print(c_total_days)
else:
    print(f"You saved the money for {c_total_days} days.")