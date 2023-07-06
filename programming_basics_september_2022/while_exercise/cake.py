width = int(input())
length = int(input())

cake_area = length * width
input_line = input()
piece_counter = 0
while input_line != "STOP":
    pieces = int(input_line)
    piece_counter += pieces
    if piece_counter > cake_area:
        break
    input_line = input()
diff = abs(piece_counter - cake_area)
if piece_counter > cake_area:
    print(f"No more cake left! You need {diff} pieces more.")
else:
    print(f"{diff} pieces are left.")
