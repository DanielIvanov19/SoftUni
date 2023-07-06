product_name = input()
quantity = int(input())

coffee_price = 1.5
water_price = 1.0
coke_price = 1.4
snacks_price = 2.0


def calc_price(product_name, quantity):
    if product_name == "coffee":
        price_res = coffee_price * quantity
        return price_res
    elif product_name == "coke":
        price_res = coke_price * quantity
        return  price_res
    elif product_name == "water":
        price_res = water_price * quantity
        return price_res
    elif product_name == "snacks":
        price_res = snacks_price * quantity
        return price_res


print(f"{calc_price(product_name, quantity):.2f}")