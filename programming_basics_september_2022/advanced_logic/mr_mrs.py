age = float(input())
gender = input()

if gender.lower() == "m":
    if age<16:
        print("Master")
    else:
        print("Mr.")
elif gender.lower() == "f":
    if age < 16:
        print("Miss")
    else:
        print("Mr.")