command = ...
final_string = ""
while True:
    command = input()
    if command == "SoftUni":
        continue
    elif command == "End":
        break
    else:
        for i in range(0, len(command)):
            final_string += command[i]*2
        print(final_string)
    final_string = ""
