inventory = {}

while True:
    line = input()
    if line == "stop":
        break
    resource = line
    line = input()
    quantity = line
    if resource not in inventory:
        inventory[resource] = int(quantity)
    else:
        inventory[resource] += int(quantity)

for item, quantity in inventory.items():
    print(f"{item} -> {quantity}")