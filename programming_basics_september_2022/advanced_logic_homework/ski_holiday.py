days = int(input())
place = input()
rating = input()
nights = days - 1

room_for_one = 18
apartment = 25
president_apartment = 35
price = 0

if place == "room for one person":
    if rating == "positive":
        price = (nights * room_for_one) * 1.25
    elif rating == "negative":
        price = (nights * room_for_one) * 0.9
elif place == "apartment":
    if nights < 10:
        price = (nights * apartment) * 0.7
        if rating == "positive":
            price = price * 1.25
        elif rating == "negative":
            price = price * 0.9
    elif 10 <= nights <= 15:
        price = (nights * apartment) * 0.65
        if rating == "positive":
            price = price * 1.25
        elif rating == "negative":
            price = price * 0.9
    elif nights > 15:
        price = (nights * apartment) * 0.5
        if rating == "positive":
            price = price * 1.25
        elif rating == "negative":
            price = price * 0.9
elif place == "president apartment":
    if nights < 10:
        price = (nights * president_apartment) * 0.9
        if rating == "positive":
            price = price * 1.25
        elif rating == "negative":
            price = price * 0.9
    elif 10 <= nights <= 15:
        price = (nights * president_apartment) * 0.85
        if rating == "positive":
            price = price * 1.25
        elif rating == "negative":
            price = price * 0.9
    elif nights > 15:
        price = (nights * president_apartment) * 0.8
        if rating == "positive":
            price = price * 1.25
        elif rating == "negative":
            price = price * 0.9
print(f"{price:.2f}")
