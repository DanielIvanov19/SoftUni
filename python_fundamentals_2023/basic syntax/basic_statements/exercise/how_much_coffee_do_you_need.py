command = input()
coffee_count = 0
while command != "END":
    upper_count = 0
    lower_count = 0
    for i in range(0, len(command)):
        if command.upper() == "CAT" or command.upper() == "DOG" or command.upper() == "CODING" or command.upper() == "MOVIE":
            if command[i].isupper():
                upper_count += 1
            else:
                lower_count += 1
        if upper_count == len(command):
            coffee_count += 2

        elif lower_count == len(command):
            coffee_count +=1
    command = input()
if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)
