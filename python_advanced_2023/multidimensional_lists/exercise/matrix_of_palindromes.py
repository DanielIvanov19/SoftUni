rows, cols = [int(el) for el in input().split()]

init_idx = 97

matrix = []

# matrix = [[str(chr(init_idx) + chr(init_idx + 1) + chr(init_idx))] and init_idx += 1 for _ in range(rows)]

for row in range(init_idx, init_idx + rows):
    for col in range(cols):
        print(f'{chr(init_idx)}{chr(init_idx + col)}{chr(init_idx)}', end=' ')

    init_idx += 1

    print()


