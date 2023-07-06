flower_type = input()
quantity = int (input())
budget = int (input())

rose = 5
dalia = 3.8
tulip = 2.8
narcis = 3
gladiola = 2.5

price = 0
difference = 0
if flower_type == "Roses":
    if quantity > 80:
        price = (quantity * rose) * 0.9
        if price > budget:
            difference = price - budget
            print(f"Not enough money, you need {difference:.2f} leva more.")
        else:
            difference = budget - price
            print(f"Hey, you have a great garden with {quantity} roses and {difference:.2f} leva left.")
    else:
        price = quantity * rose
        if price > budget:
            difference = price - budget
            print(f"Not enough money, you need {difference:.2f} leva more.")
        else:
            difference = budget - price
            print(f"Hey, you have a great garden with {quantity} roses and {difference:.2f} leva left.")

if flower_type == "Dahlias":
    if quantity > 90:
        price = (quantity * dalia) * 0.85
        if price > budget:
            difference = price - budget
            print(f"Not enough money, you need {difference:.2f} leva more.")
        else:
            difference = budget - price
            print(f"Hey, you have a great garden with {quantity} dahlias and {difference:.2f} leva left.")
    else:
        price = quantity * dalia
        if price > budget:
            difference = price - budget
            print(f"Not enough money, you need {difference:.2f} leva more.")
        else:
            difference = budget - price
            print(f"Hey, you have a great garden with {quantity} dahlias and {difference:.2f} leva left.")

if flower_type == "Tulips":
    if quantity > 80:
        price = (quantity * tulip) * 0.85
        if price > budget:
            difference = price - budget
            print(f"Not enough money, you need {difference:.2f} leva more.")
        else:
            difference = budget - price
            print(f"Hey, you have a great garden with {quantity} tulips and {difference:.2f} leva left.")
    else:
        price = quantity * tulip
        if price > budget:
            difference = price - budget
            print(f"Not enough money, you need {difference:.2f} leva more.")
        else:
            difference = budget - price
            print(f"Hey, you have a great garden with {quantity} tulips and {difference:.2f} leva left.")

if flower_type == "Daffodil":
    if quantity < 120:
        price = (quantity * narcis) * 1.15
        if price > budget:
            difference = price - budget
            print(f"Not enough money, you need {difference:.2f} leva more.")
        else:
            difference = budget - price
            print(f"Hey, you have a great garden with {quantity} daffodils and {difference:.2f} leva left.")
    else:
        price = quantity * narcis
        if price > budget:
            difference = price - budget
            print(f"Not enough money, you need {difference:.2f} leva more.")
        else:
            difference = budget - price
            print(f"Hey, you have a great garden with {quantity} daffodils and {difference:.2f} leva left.")

if flower_type == "Gladioli":
    if quantity < 80:
        price = (quantity * gladiola) * 1.2
        if price > budget:
            difference = price - budget
            print(f"Not enough money, you need {difference:.2f} leva more.")
        else:
            difference = budget - price
            print(f"Hey, you have a great garden with {quantity} gladioli and {difference:.2f} leva left.")
    else:
        price = quantity * gladiola
        if price > budget:
            difference = price - budget
            print(f"Not enough money, you need {difference:.2f} leva more.")
        else:
            difference = budget - price
            print(f"Hey, you have a great garden with {quantity} gladioli and {difference:.2f} leva left.")