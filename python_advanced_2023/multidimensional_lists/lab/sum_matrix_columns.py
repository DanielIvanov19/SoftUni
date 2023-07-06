rows, columns = [int(el) for el in input().split(', ')]

matrix = [[int(el) for el in input().split()] for _ in range(rows)]
sum_els = 0
for columns in range(columns):
    for row in range(rows):
        sum_els += matrix[row][columns]
    print(sum_els)
    if row == 2:
        sum_els = 0
