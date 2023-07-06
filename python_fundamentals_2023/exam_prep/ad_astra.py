import re

food_input = input()

pattern = r"(?P<start>[#|])(?P<food>[A-Za-z\s]+)\1(?P<Date>[0-9]{2}\/[0-9]{2}\/[0-9]{2})\1(?P<calories>[0-9]{1,5})\1"

matches = re.findall(pattern, food_input)
total_calories = 0
products = []
for match in matches:
    product = match[1]
    exp_date = match[2]
    calories = int(match[3])
    products.append(f"Item: {product}, Best before: {exp_date}, Nutrition: {calories}")
    total_calories += calories

days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
print('\n'.join(products))
