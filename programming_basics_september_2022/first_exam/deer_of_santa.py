import math
absent = int(input())
food_left = int(input())
first_deer = float(input())
second_deer = float(input())
third_deer = float(input())

first_deer_food = first_deer * absent
second_deer_food = second_deer * absent
third_deer_food = third_deer * absent
needed_food = first_deer_food + second_deer_food + third_deer_food

if food_left >= needed_food:
    print(f"{math.floor(food_left - needed_food)} kilos of food left.")
elif needed_food > food_left:
    print(f"{math.ceil(needed_food -food_left)} more kilos of food are needed.")
