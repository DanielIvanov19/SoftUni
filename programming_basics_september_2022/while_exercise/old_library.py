old_book = input()
counter = 0
is_found = False
book = input()
while book != "No More Books":
    if book == old_book:
        is_found = True
        break
    counter += 1
    book = input()
if is_found:
    print(f"You checked {counter} books and found it.")
else:
    print("The book you searched is not here!")
    print(f"You checked {counter} books.")
