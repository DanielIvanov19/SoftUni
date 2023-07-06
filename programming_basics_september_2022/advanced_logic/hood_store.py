product = input()
city = input()
quantity = float(input())

if city == "Sofia":
    if product == "coffee":
        price = quantity*0.5
        print(price)
    elif product == "water":
        price = quantity*0.8
        print(price)
    elif product == "beer":
        price = quantity*1.2
        print(price)
    elif product == "sweets":
        price = quantity*1.45
        print(price)
    elif product == "peanuts":
        price = quantity*1.6
        print(price)
elif city == "Plovdiv":
    if product == "coffee":
        price = quantity*0.4
        print(price)
    elif product == "water":
        price = quantity*0.7
        print(price)
    elif product == "beer":
        price = quantity*1.15
        print(price)
    elif product == "sweets":
        price = quantity*1.3
        print(price)
    elif product == "peanuts":
        price = quantity*1.5
        print(price)
elif city == "Varna":
    if product == "coffee":
        price = quantity*0.45
        print(price)
    elif product == "water":
        price = quantity*0.7
        print(price)
    elif product == "beer":
        price = quantity*1.1
        print(price)
    elif product == "sweets":
        price = quantity*1.35
        print(price)
    elif product == "peanuts":
        price = quantity*1.55
        print(price)