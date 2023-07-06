import re

total_cost = 0

pattern = r">>([A-Za-z]+)<<(\d+(\.\d+)?)!(\d+)"

bought_items = []

while True:
    line = input()
    if line == "Purchase":
        break

    matches = re.findall(pattern, line)
    if not matches:
        continue

    for match in matches:
        item = match[0]
        price = float(match[1])
        quantity = int(match[3])

        bought_items.append(item)
        total_cost += price * quantity

print("Bought furniture:")
if len(bought_items) != 0:
    print('\n'.join(bought_items))
print(f"Total money spend: {total_cost:.2f}")
