import operator
from collections import deque
from colorama import Fore


def get_circles_count(row, col, dx, dy, operator_func):
    current_count = 0
    for i in range(1, 4):
        new_row = operator_func(row, dx * i)
        new_col = operator_func(col, dy * i)

        if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
            break

        if board[new_row][new_col] != player_symbol:
            break
        current_count += 1
    return current_count


def place_circle():
    row = 0

    while row != ROWS and board[row][player_col] == "0":
        row += 1
    board[row - 1][player_col] = player_symbol
    return row - 1


def check_for_win(row, col):
    for x, y in directions:
        count = get_circles_count(row, col, x, y, operator.add) + get_circles_count(row, col, x, y, operator.sub) + 1

        if count >= 4:
            return True

    if count_draw == ROWS * COLS:
        print_board()
        print('Draw!')
        raise SystemExit

    return False


def print_board():
    [print(f"[ {', '.join(row)} ]") for row in board]


ROWS, COLS = 6, 7

count_draw = 0

board = [['0'] * COLS for row in range(ROWS)]

player_one = Fore.GREEN + '1' + Fore.RESET
player_two = Fore.BLUE + '2' + Fore.RESET

turns = deque([[1, player_one], [2, player_two]])

win = False

directions = (
    (1, 0),  # down
    (0, -1),  # left
    (-1, -1),  # top left
    (-1, 1),  # top right
)

while not win:
    print_board()

    player_num, player_symbol = turns[0]

    try:
        player_col = int(input(f'Player {player_num}, please choose a column: ')) - 1

    except ValueError:
        print(Fore.RED + f'Enter a valid number in the range (1-{COLS})' + Fore.RESET)
        continue

    if not 0 <= player_col < COLS:
        print(Fore.RED + f'Enter a valid number in the range (1-{COLS})' + Fore.RESET)
        continue

    if board[0][player_col] != '0':
        print(Fore.RED + 'No empty spaces left on that row, please choose another one' + Fore.RESET)
        continue

    row = place_circle()
    count_draw += 1
    win = check_for_win(row, player_col)

    turns.rotate()
print_board()
print(f'Player {turns[1][0]} wins!')
