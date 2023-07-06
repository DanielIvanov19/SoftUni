nylon_per_square_meter = 1.5
paint_per_liter = 14.5
solvent_per_liter = 5
bags = 0.4
nylon_quantity = int(input())
paint_quantity = int(input())
solvent_quantity = int(input())
work_hours = int(input())
paint_sum = (paint_quantity + paint_quantity*10/100)*paint_per_liter
nylon_sum = (nylon_quantity + 2)*nylon_per_square_meter
workers_total = ((paint_sum + nylon_sum + solvent_quantity*solvent_per_liter + bags)*30/100)*work_hours
total_sum = paint_sum + nylon_sum + solvent_quantity*solvent_per_liter + bags + workers_total
print(total_sum)