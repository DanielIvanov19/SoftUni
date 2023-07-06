from collections import deque


def choose_pos():
    while True:
        try:
            position = int(input(f'{players[0][0]} choose a free position in range (1-{SIZE * SIZE}): '))
            row, col = (position - 1) // SIZE, (position - 1) % SIZE
            
        except ValueError:
            print(f'{players[0][0]}, please select a valid position!')
            continue

        if 0 <= position <= SIZE * SIZE:
            pass
        else:
            print(f'{players[0][0]}, please select a valid position!')


def print_board(begin=False):
    if begin:
        print('This is the numeration of the board:')
        [print(f"| {' | '.join(row)} |") for row in board]

        for row in range(SIZE):
            for col in range(SIZE):
                board[row][col] = ' '

    else:
        [print(f"| {' | '.join(row)} |") for row in board]


def start():
    player_one_name = input('Player one, please enter your name: ')
    player_two_name = input('Player two, please enter your name: ')

    while True:
        player_one_symbol = input(f"{player_one_name} what symbol would you like to play with(X/0)?")

        if player_one_symbol not in ['X', 'O']:
            print(f"{player_one_name}, please select a valid symbol!")
        else:
            break
    player_two_symbol = 'O' if player_one_symbol == 'X' else 'X'

    players.append([player_one_name, player_one_symbol])
    players.append([player_two_name, player_two_symbol])

    print_board(begin=True)


SIZE = 3

board = [[str(i), str(i + 1), str(i + 2)] for i in range(1, SIZE * SIZE + 1, SIZE)]
players = deque()

start()
