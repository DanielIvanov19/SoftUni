from sys import maxsize
field_size = int(input())

matrix = []
bunny_coordinates = []
max_path = []
max_eggs = -maxsize
max_command = None

# find the bunny's coordinates
for row in range(field_size):
    matrix.append(input().split())

    if 'B' in matrix[row]:
        bunny_coordinates = [row, matrix[row].index('B')]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


for direction, positions in directions.items():
    currents_max = 0
    current_path = []

    r, c = [
        bunny_coordinates[0] + positions[0],
        bunny_coordinates[1] + positions[1]
    ]
    # if (r < 0 or r >= field_size) or (c < 0 or c >= field_size):
    #    continue

    while 0 <= r < field_size and 0 <= c < field_size:
        if matrix[r][c] == 'X':
            break

        currents_max += int(matrix[r][c])
        current_path.append([r, c])

        r += positions[0]
        c += positions[1]

    if currents_max >= max_eggs:
        max_eggs = currents_max
        max_command = direction
        max_path = current_path

print(max_command)
print(*max_path, sep='\n')
print(max_eggs)
