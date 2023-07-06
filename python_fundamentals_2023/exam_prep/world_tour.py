user_input = input()

while True:
    command = input()
    if command == "Travel":
        break
    if command.split(':')[0] == "Add Stop":
        index_stop = int(command.split(':')[1])
        destination = command.split(':')[2]
        if 0 <= index_stop <= len(user_input):
            user_input = user_input[:index_stop] + destination + user_input[index_stop:]

    elif command.split(':')[0] == "Remove Stop":
        start_idx = int(command.split(':')[1])
        end_idx = int(command.split(':')[2])
        if 0 <= start_idx < len(user_input) and 0 <= end_idx < len(user_input):
            # text_removal = user_input[start_idx:end_idx + 1]
            # user_input = user_input.replace(text_removal, '')
            user_input = user_input[:start_idx] + user_input[end_idx + 1:]

    else:
        old_string = command.split(':')[1]
        new_string = command.split(':')[2]
        user_input = user_input.replace(old_string, new_string)
    print(user_input)
print(f"Ready for world tour! Planned stops: {user_input}")
