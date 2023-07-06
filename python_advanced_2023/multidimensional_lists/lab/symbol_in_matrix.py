n = int(input())

matrix = [[str(el) for el in input()] for _ in range(n)]

seeked_symbol = input()
final_message = ''
for i in range(n):
    for j in range(n):
        if matrix[i][j] == seeked_symbol:
            final_message = f'({i}, {j})'
            print(final_message)
            break
if final_message == '':
    print(f"{seeked_symbol} does not occur in the matrix")
