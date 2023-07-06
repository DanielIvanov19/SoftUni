budget = float(input())
season = input()
destination = ""
place = ""
expenses = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        expenses = budget * 0.3
        place = "Camp"
    elif season == "winter":
        expenses = budget * 0.7
        place = "Hotel"
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        expenses = budget * 0.4
        place = "Camp"
    elif season == "winter":
        expenses = budget * 0.8
        place = "Hotel"
elif budget > 1000:
    destination = "Europe"
    expenses = budget * 0.9
    place = "Hotel"

print(f"Somewhere in {destination}")
print(f"{place} - {expenses:.2f}")
