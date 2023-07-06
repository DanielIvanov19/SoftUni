rows, cols = (int(x) for x in input().split(','))

directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

cupboard_area = []
for _ in range(rows):
    row = input()
    cupboard_area.append(list(row))

cheese_found = sum(row.count('C') for row in cupboard_area)

current_pos = []
while True:
    pos_found = False
    for row in range(rows):
        for col in range(cols):
            if cupboard_area[row][col] == 'M':
                current_pos = [row, col]
                pos_found = True
                break
        if pos_found:
            break

    command = input()
    if command == 'danger':
        print("Mouse will come back later!")
        break

    if command in directions:
        next_pos = directions[command](*current_pos)
        next_row, next_col = next_pos[0], next_pos[1]

        if not (0 <= next_row < rows and 0 <= next_col < cols):
            print("No more cheese for tonight!")
            break

        next_pos_value = cupboard_area[next_row][next_col]
        if next_pos_value == 'C':
            cupboard_area[current_pos[0]][current_pos[1]] = '*'
            cupboard_area[next_row][next_col] = 'M'
            current_pos = [next_row, next_col]
            cheese_found -= 1
            if cheese_found == 0:
                print("Happy mouse! All the cheese is eaten, good night!")
                break
        elif next_pos_value == 'T':
            cupboard_area[current_pos[0]][current_pos[1]] = '*'
            cupboard_area[next_row][next_col] = 'M'
            current_pos = [next_row, next_col]
            print("Mouse is trapped!")
            break
        elif next_pos_value == '@':
            continue

# Print the final state of the matrix
for row in cupboard_area:
    print(''.join(row))
