rows_cols = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(rows_cols)]

i = 0
j = 0

sum_diagonal = 0

while i < rows_cols and j < rows_cols:
    sum_diagonal += matrix[i][j]
    i += 1
    j += 1

print(sum_diagonal)
