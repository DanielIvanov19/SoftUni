price_products = {}

quantity_products = {}

while True:
    line = input()
    if line == "buy":
        break

    args = line.split()
    product = args[0]
    price = float(args[1])
    quantity = int(args[2])

    if product in price_products:
        price_products[product] = price
        quantity_products[product] += quantity

    else:
        price_products[product] = price
        quantity_products[product] = quantity

for product in price_products:
    price = price_products[product]
    quantity = quantity_products[product]
    total_price = price * quantity
    print(f"{product} -> {total_price:.2f}")