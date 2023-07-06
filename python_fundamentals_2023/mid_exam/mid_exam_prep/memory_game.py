num_sequence = input().split(' ')

command = input()
moves = 0
has_won = False
while command != "end":
    moves += 1
    first_index = int(command.split(' ')[0])
    second_index = int(command.split(' ')[1])
    length_of_sequence = len(num_sequence)
    if (0 <= first_index < length_of_sequence and 0 <= second_index < length_of_sequence) \
            and first_index != second_index:
        if num_sequence[first_index] == num_sequence[second_index]:
            element_for_removal = num_sequence[first_index]
            num_sequence.remove(element_for_removal)
            num_sequence.remove(element_for_removal)
            print(f"Congrats! You have found matching elements - {element_for_removal}!")

            if len(num_sequence) == 0:
                print(f"You have won in {moves} turns!")
                has_won = True
                exit(0)
        else:
            print("Try again!")
    else:
        print(f"Invalid input! Adding additional elements to the board")
        half = len(num_sequence) // 2
        num_sequence.insert(half, f"-{moves}a")
        num_sequence.insert(half + 1, f"-{moves}a")
    command = input()
if command == "end":
    if has_won != True:
        output_string = ' '.join(num_sequence)
        print(f"Sorry you lose :(\n"
              f"{output_string}")
