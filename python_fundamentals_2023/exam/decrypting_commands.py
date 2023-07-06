user_input = input()

while True:
    line = input()
    if line == "Finish":
        break

    command_args = line.split()

    main_command = command_args[0]

    if main_command == "Replace":
        curr_char = command_args[1]
        new_char = command_args[2]
        user_input = user_input.replace(curr_char, new_char)
        print(user_input)

    elif main_command == "Cut":
        start_idx = int(command_args[1])
        end_idx = int(command_args[2])
        if 0 <= start_idx < len(user_input) and 0 <= end_idx < len(user_input):
            user_input = user_input[:start_idx] + user_input[end_idx + 1:]
            print(user_input)
        else:
            print("Invalid indices!")
    elif main_command == "Make":
        up_down = command_args[1]
        if up_down == "Upper":
            user_input = user_input.upper()
            print(user_input)
        elif up_down == "Lower":
            user_input = user_input.lower()
            print(user_input)

    elif main_command == "Check":
        check = command_args[1]
        if check in user_input:
            print(f"Message contains {check}")
        else:
            print(f"Message doesn't contain {check}")

    elif main_command == "Sum":
        start_idx = int(command_args[1])
        end_idx = int(command_args[2])
        if 0 <= start_idx < len(user_input) and 0 <= end_idx < len(user_input):
            substr = user_input[start_idx:end_idx+1]
            sum_ascii = 0
            for char in substr:
                sum_ascii += ord(char)
            print(sum_ascii)
        else:
            print("Invalid indices!")


