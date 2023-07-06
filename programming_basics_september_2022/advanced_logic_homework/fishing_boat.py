spring = 3000
summer = 4200
autumn = 4200
winter = 2600

budget = int(input())
season = input()
people = int(input())

price = 0
if people <= 6:
    if season == "Spring":
        price = spring*0.9
        if people % 2 == 0:
            price = price * 0.95
    elif season == "Summer":
        price = summer * 0.9
        if people % 2 == 0:
            price = price * 0.95
    elif season == "Autumn":
        price = autumn * 0.9
    elif season == "Winter":
        price = autumn * 0.85
        if people % 2 == 0:
            price = price * 0.95
elif 7 <= people <= 11:
    if season == "Spring":
        price = spring*0.85
        if people % 2 == 0:
            price = price * 0.95
    elif season == "Summer":
        price = summer * 0.85
        if people % 2 == 0:
            price = price * 0.95
    elif season == "Autumn":
        price = autumn * 0.85
    elif season == "Winter":
        price = autumn * 0.85
        if people % 2 == 0:
            price = price * 0.95
elif people >= 12:
    if season == "Spring":
        price = spring*0.75
        if people % 2 == 0:
            price = price * 0.95
    elif season == "Summer":
        price = summer * 0.75
        if people % 2 == 0:
            price = price * 0.95
    elif season == "Autumn":
        price = autumn * 0.75
    elif season == "Winter":
        price = autumn * 0.75
        if people % 2 == 0:
            price = price * 0.95

if budget > price:
    difference = budget - price
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    difference = price - budget
    print(f"Not enough money! You need {difference:.2f} leva.")
