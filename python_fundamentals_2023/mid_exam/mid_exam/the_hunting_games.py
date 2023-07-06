days = int(input())
players = int(input())
group_energy = float(input())
water_per_day_per_person = float(input())
food_per_day_per_person = float(input())

water_amount = players * water_per_day_per_person * days
food_amount = players * food_per_day_per_person * days
is_energized = True
for day in range(1, days + 1):
    chopped_energy = float(input())
    group_energy -= chopped_energy
    if group_energy <= 0:
        print(f"You will run out of energy. You will be left with {food_amount:.2f} food and {water_amount:.2f} water.")
        is_energized = False
        exit(0)
    if day % 2 == 0:
        group_energy += group_energy * (5 / 100)
        water_amount -= water_amount * (30 / 100)
    if day % 3 == 0:
        food_amount -= food_amount / players
        group_energy += group_energy * (10 / 100)

if is_energized:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
