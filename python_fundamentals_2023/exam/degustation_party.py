guests_meals = {}
disliked = 0
while True:
    line = input()
    if line == "Stop":
        break
    command_args = line.split("-")
    like_dislike = command_args[0]
    guest = command_args[1]
    meal = command_args[2]

    if like_dislike == "Like":

        if guest not in guests_meals:
            guests_meals[guest] = []
            guests_meals[guest].append(meal)
        else:
            if meal in guests_meals[guest]:
                continue
            else:
                guests_meals[guest].append(meal)

    elif like_dislike == "Dislike":
        if guest not in guests_meals:
            print(f"{guest} is not at the party.")
        else:
            if meal in guests_meals[guest]:
                print(f"{guest} doesn't like the {meal}.")
                guests_meals[guest].remove(meal)
                disliked += 1
            else:
                print(f"{guest} doesn't have the {meal} in his/her collection.")

for guest, meals in guests_meals.items():
    meals_g = ', '.join(guests_meals[guest])
    print(f"{guest}: {meals_g}")
print(f"Unliked meals: {disliked}")