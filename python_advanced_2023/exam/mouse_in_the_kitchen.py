rows, cols = (int(x) for x in input().split(','))

directions = {
    'up': lambda r, c: [(r - 1) , c],  # (-1, 0),
    'down': lambda r, c: [(r + 1) , c],  # (1, 0),
    'left': lambda r, c: [r, (c - 1)],  # (0, -1),
    'right': lambda r, c: [r, (c + 1)],  # (0, 1)
}


cupboard_area = []
for _ in range(rows):
    row = input()
    cupboard_area.append(list(row))

cheese_found = 0

for row in range(rows):
    for col in range(cols):
        if cupboard_area[row][col] == 'C':
            cheese_found += 1


while True:
    current_pos = []
    pos_found = False
    for row in range(rows):
        for col in range(cols):
            if cupboard_area[row][col] == 'M':
                current_pos.append(row)
                current_pos.append(col)
                pos_found = True
                break
        if pos_found:
            break

    command = input()
    if command == 'danger':
        print("Mouse will come back later!")
        break
    if command in directions:

        mouse_next_pos = directions[command](current_pos[0], current_pos[1])

        if (mouse_next_pos[0] < 0 or mouse_next_pos[0] > rows - 1) or (mouse_next_pos[1] < 0 or mouse_next_pos[1] > cols - 1):
            print("No more cheese for tonight!")
            break
        elif cupboard_area[mouse_next_pos[0]][mouse_next_pos[1]] == "@":
            continue
        elif cupboard_area[mouse_next_pos[0]][mouse_next_pos[1]] == "T":
            prev_pos_1 = current_pos[0]
            prev_pos_2 = current_pos[1]

            next_pos_1 = mouse_next_pos[0]
            next_pos_2 = mouse_next_pos[1]

            cupboard_area[prev_pos_1][prev_pos_2] = "*"
            cupboard_area[next_pos_1][next_pos_2] = "M"

            print("Mouse is trapped!")
            break

        elif cupboard_area[mouse_next_pos[0]][mouse_next_pos[1]] == "C":
            cheese_found -= 1

            prev_pos_1 = current_pos[0]
            prev_pos_2 = current_pos[1]

            next_pos_1 = mouse_next_pos[0]
            next_pos_2 = mouse_next_pos[1]

            cupboard_area[prev_pos_1][prev_pos_2] = "*"
            cupboard_area[next_pos_1][next_pos_2] = "M"

            if cheese_found < 1:
                print("Happy mouse! All the cheese is eaten, good night!")
                break
        elif cupboard_area[mouse_next_pos[0]][mouse_next_pos[1]] == "*":
            prev_pos_1 = current_pos[0]
            prev_pos_2 = current_pos[1]

            next_pos_1 = mouse_next_pos[0]
            next_pos_2 = mouse_next_pos[1]

            cupboard_area[prev_pos_1][prev_pos_2] = "*"
            cupboard_area[next_pos_1][next_pos_2] = "M"

for x in range(rows):
    print(''.join(cupboard_area[x]))