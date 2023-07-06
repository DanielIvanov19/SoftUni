import random
player_number=...
computer_number = random.randint(1, 100)
print(computer_number)
print("Enter a number between 1 and 100 and try to guess the cpu's number: ")
while player_number != computer_number:
    player_input = input()
    if not player_input.isdigit():
        print("Invalid input")
        continue
    else:
        player_number = int(player_input)
    if player_number > computer_number:
        print("Your number is bigger than the cpu's number, try again")
    elif player_number < computer_number:
        print("Your number is less than cpu's number, try again")
else:
    print(f"You guessed the number is: {computer_number}")
