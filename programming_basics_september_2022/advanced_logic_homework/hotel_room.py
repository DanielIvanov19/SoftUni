month = input()
days = int(input())

total_studio = 0
total_apartment = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if 7 < days <= 14:
        total_studio = (studio_price * days) * 0.95
        total_apartment = apartment_price * days
    elif days > 14:
        total_studio = (studio_price * days) * 0.7
        total_apartment = (apartment_price * days) * 0.9
    else:
        total_studio = studio_price * days
        total_apartment = apartment_price * days
elif month == "June" or month == "September":
    studio_price = 75.2
    apartment_price = 68.7
    if days > 14:
        total_studio = studio_price * 0.8 * days
        total_apartment = apartment_price * 0.9 * days
    else:
        total_studio = studio_price * days
        total_apartment = apartment_price * days
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
    total_studio = studio_price * days
    if days > 14:
        total_apartment = (apartment_price * days) * 0.9
    else:
        total_apartment = apartment_price * days
print(f"Apartment: {total_apartment:.2f} lv.")
print(f"Studio: {total_studio:.2f} lv.")
