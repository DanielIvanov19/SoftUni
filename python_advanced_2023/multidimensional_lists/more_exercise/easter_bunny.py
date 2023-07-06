from sys import maxsize
field_size = int(input())

matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(field_size)]
bunny_coordinates = []
max_eggs = -maxsize
max_command = None

# find the bunny's coordinates
for row in range(field_size):
    for col in range(field_size):
        if matrix[row][col] == 'B':
            bunny_coordinates.append(row)
            bunny_coordinates.append(col)
            break

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


for direction in directions:
    currents_max = 0

    r = bunny_coordinates[0] + directions[direction][0]
    c = bunny_coordinates[1] + directions[direction][1]
    # if (r < 0 or r >= field_size) or (c < 0 or c >= field_size):
    #    continue

    while 0 <= r < field_size and 0 <= c < field_size:
        if matrix[r][c] == 'X':
            break

        currents_max += int(matrix[r][c])
        r += directions[direction][0]
        c += directions[direction][1]

    if currents_max >= max_eggs:
        max_eggs = currents_max
        max_command = direction

print(max_command)
r = bunny_coordinates[0] + directions[max_command][0]
c = bunny_coordinates[1] + directions[max_command][1]
while 0 <= r < field_size and 0 <= c < field_size:
    print([r, c])
    r += directions[max_command][0]
    c += directions[max_command][1]
print(max_eggs)
