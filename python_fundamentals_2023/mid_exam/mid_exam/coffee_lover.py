coffee_list = input().split(" ")
commands = int(input())


for _ in range(commands):
    command_input = input()
    command = command_input.split(" ")[0]
    if command == "Include":
        coffee_add = command_input.split(" ")[1]
        coffee_list.append(coffee_add)
    elif command == "Remove":
        first_last = command_input.split(" ")[1]
        number_coffees = int(command_input.split(" ")[2])
        if first_last == "first":
            if number_coffees <= len(coffee_list):
                for _ in range(number_coffees):
                    coffee_list.pop(0)
        elif first_last == "last":
            if number_coffees <= len(coffee_list):
                for _ in range(number_coffees):
                    coffee_list.pop(-1)
    elif command == "Prefer":
        coffee_index_1 = int(command_input.split(" ")[1])
        coffee_index_2 = int(command_input.split(" ")[2])

        if 0 <= coffee_index_1 <= len(coffee_list) - 1 and 0 <= coffee_index_2 <= len(coffee_list) - 1:
            coffee_list[coffee_index_1], coffee_list[coffee_index_2] = coffee_list[coffee_index_2], coffee_list[coffee_index_1]

    elif command == "Reverse":
        coffee_list.reverse()
coffee_list_to_string = ' '.join(coffee_list)
print(f"Coffees:\n"
      f"{coffee_list_to_string}")
