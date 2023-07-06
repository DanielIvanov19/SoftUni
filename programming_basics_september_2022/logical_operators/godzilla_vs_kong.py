budget = float(input())
stat_count = int(input())
outfit_price = float(input())
decor_price = budget*0.1

if stat_count > 150:
    outfit_price = (stat_count*outfit_price)*0.9
else:
    outfit_price = stat_count*outfit_price
total = outfit_price + decor_price
difference = abs(budget-total)

if total > budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")