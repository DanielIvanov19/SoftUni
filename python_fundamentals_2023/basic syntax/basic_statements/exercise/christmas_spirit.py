quantity = int(input())
days_to_christmas = int(input())

ornament_set_price = 2
ornament_set_pts = 5

tree_skirt_price = 5
tree_skirt_pts = 3

tree_garland_price = 3
tree_garland_pts = 10

tree_lights_price = 15
tree_lights_pts = 17

points_total = 0
price_total = 0
days = 1
for i in range(0, days_to_christmas):
    if days % 11 == 0:
        quantity += 2
    if days % 2 == 0:
        price_total += quantity*ornament_set_price
        points_total += ornament_set_pts
    if days % 3 == 0:
        price_total += quantity * tree_skirt_price + quantity * tree_garland_price
        points_total += tree_skirt_pts + tree_garland_pts
    if days % 5 == 0:
        price_total += quantity * tree_lights_price
        points_total += tree_lights_pts
    if days % 10 == 0:
        points_total -= 20
        price_total += tree_skirt_price + tree_garland_price + tree_lights_price
    if days % 15 == 0:
        points_total += 30
    days += 1
if days_to_christmas % 10 == 0:
    points_total -= 30

print(f"Total cost: {price_total}")
print(f"Total spirit: {points_total}")
