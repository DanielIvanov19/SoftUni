def move(direction, steps):
    r = my_pos[0] + (directions[direction][0] * steps)
    c = my_pos[1] + (directions[direction][1] * steps)

    if not(0 <= r < SIZE and 0 <= c < SIZE):
        return my_pos
    if field[r][c] == "x":
        return my_pos

    return [r, c]


def shoot(direction):
    r = my_pos[0] + directions[direction][0]
    c = my_pos[1] + directions[direction][1]

    while 0 <= r < SIZE and 0 <= c < SIZE:
        if field[r][c] == 'x':
            field[r][c] = '.'
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]


SIZE = 5  # means a constant variable
field = []

targets = 0
targets_hit = 0
targets_hit_coordinates = []

my_pos = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(SIZE):
    field.append(input().split())

    if 'A' in field[row]:
        my_pos = [row, field[row].index('A')]

    targets += field[row].count('x')

for _ in range(int(input())):
    command = input().split()

    if command[0] == 'move':
        my_pos = move(command[1], int(command[2]))
    elif command[0] == 'shoot':
        targets_down_coordinates = shoot(command[1])

        if targets_down_coordinates:
            targets_hit_coordinates.append(targets_down_coordinates)
            targets_hit += 1
        if targets_hit == targets:
            print(f'Training completed! All {targets} targets hit.')
            break
else:
    print(f'Training not completed! {targets - targets_hit} targets left.')

print(*targets_hit_coordinates, sep='\n')
