data = input()
products = {}

while data != "statistics":
    key, value = data.split(": ")
    value = int(value)
    if key in products.keys():
        products[key] += value
    else:
        products[key] = value
    data = input()

print("Products in stock:")

for key, value in products.items():
    print(f"- {key}: {value}")
total_products = len(products)

print(f"Total Products: {total_products}")
print(f"Total Quantity: {sum(products.values())}")
