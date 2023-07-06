cards = input().split(", ")
n = int(input())

for _ in range(n):
    command_input = input()
    command = command_input.split(", ")[0]
    if command == "Add":
        card_name = command_input.split(", ")[1]
        if card_name not in cards:
            cards.append(card_name)
            print("Card successfully added")
        else:
            print("Card is already in the deck")
    elif command == "Remove":
        card_name = command_input.split(", ")[1]
        if card_name in cards:
            cards.remove(card_name)
            print("Card successfully removed")
        else:
            print("Card not found")
    elif command == "Remove At":
        card_index = int(command_input.split(", ")[1])
        if 0 <= card_index <= len(cards) - 1:
            cards.pop(card_index)
            print("Card successfully removed")
        else:
            print("Index out of range")
    elif command == "Insert":
        card_index = int(command_input.split(", ")[1])
        card_name = command_input.split(", ")[2]
        if 0 <= card_index <= len(cards) - 1:
            if card_name not in cards:
                cards.insert(card_index, card_name)
                print("Card successfully added")
            else:
                print("Card is already added")
        else:
            print("Index out of range")

print(', '.join(cards))
