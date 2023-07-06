ticket_price = 150
markup = 1.4
items_input = input().split("|")
budget = float(input())

clothes_max = 50.0
shoes_max = 35.0
accessories_max = 20.5

prices_list = []
for item in items_input:
    item_args = item.split("->")
    item_name = item_args[0]
    item_price = float(item_args[1])

    if item_name == "Clothes":
        if clothes_max < item_price:
            continue
        else:
            if budget >= item_price:
                #count = budget // item_price
                prices_list.append(item_price)
                budget -= item_price
            else:
                continue
    elif item_name == "Shoes":
        if shoes_max < item_price:
            continue
        else:
            if budget >= item_price:
                #count = budget // item_price
                prices_list.append(item_price)
                budget -= item_price
            else:
                continue
    elif item_name == "Accessories":
        if accessories_max < item_price:
            continue
        else:
            if budget >= item_price:
                #count = budget // item_price
                prices_list.append(item_price)
                budget -= item_price
            else:
                continue

sum_init = 0
sum_new = 0
for price in prices_list:
    sum_init += price
new_price_list = []
for item in prices_list:
    new_price = round(item * 1.4, 2)
    new_price_list.append(new_price)
for price in new_price_list:
    sum_new = sum_new + price

profit = sum_new - sum_init

#print(new_price_list)
for price in new_price_list:
    print(f"{price:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if budget + sum_new >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")
