budget = float(input())
num_nights = int(input())
price_per_night = float(input())
percent_additional_expenses = int(input())

if num_nights > 7:
    price_per_night -= price_per_night * 0.05
costs = num_nights * price_per_night
print(costs)
additional_expenses = budget * (percent_additional_expenses / 100)
total_costs = costs + additional_expenses
diff = abs(budget - total_costs)

if budget >= total_costs:
    print(f"Ivanovi will be left with{diff:.2f} leva after vacation.")
else:
    print(f"{diff} leva needed.")