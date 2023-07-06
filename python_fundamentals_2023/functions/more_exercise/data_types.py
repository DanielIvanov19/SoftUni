command = input()
user_input = input()


def data_type(command, input_str):
    if command == "int":
        return int(input_str) * 2
    elif command == "real":
        return f"{float(input_str) * 1.5:.2f}"
    elif command == "string":
        return f"${input_str}$"


result = data_type(command, user_input)
print(result)
