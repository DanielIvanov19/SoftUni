num_days = int(input())
num_hours = int(input())
total_costs = 0

for day in range(1, num_days + 1):
    current_cost = 0
    for hour in range(1, num_hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            current_cost += 2.5
            total_costs += 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            current_cost += 1.25
            total_costs += 1.25
        else:
            current_cost += 1
            total_costs += 1
    print(f'Day: {day} - {current_cost:.2f} leva.')