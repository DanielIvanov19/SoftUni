def cookie_eating(presents_left, good_kids):
    for coordinates in directions.values():
        r = santa_coordinates[0] + coordinates[0]
        c = santa_coordinates[1] + coordinates[1]

        if neighbourhood[r][c].isalpha():
            if neighbourhood[r][c] == 'V':
                good_kids += 1
            neighbourhood[r][c] = '-'
            presents_left -= 1

        if not presents_left:
            break

    return presents_left, good_kids


all_presents = int(input())
SIZE = int(input())

neighbourhood = []
santa_coordinates = []
all_good_kids = 0
good_kids_visited = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(SIZE):
    line = input().split()

    neighbourhood.append(line)

    if 'S' in line:
        santa_coordinates = [row, line.index('S')]
        neighbourhood[row][santa_coordinates[1]] = '-'

    all_good_kids += line.count('V')

command = input()

while command != 'Christmas morning':

    santa_coordinates[0] += directions[command][0]
    santa_coordinates[1] += directions[command][1]

    house = neighbourhood[santa_coordinates[0]][santa_coordinates[1]]

    if house == 'V':
        good_kids_visited += 1
        all_presents -= 1
    elif house == 'C':
        all_presents, good_kids_visited = cookie_eating(all_presents, good_kids_visited)

    neighbourhood[santa_coordinates[0]][santa_coordinates[1]] = '-'

    if not all_presents or good_kids_visited == all_good_kids:
        break

    command = input()

neighbourhood[santa_coordinates[0]][santa_coordinates[1]] = 'S'

if not all_presents and good_kids_visited < all_good_kids:
    print('Santa ran out of presents!')

print(*[' '.join(line) for line in neighbourhood], sep='\n')

if all_good_kids == good_kids_visited:
    print(f'Good job, Santa! {all_good_kids} happy nice kid/s.')
else:
    print(f'No presents for {all_good_kids - good_kids_visited} nice kid/s.')