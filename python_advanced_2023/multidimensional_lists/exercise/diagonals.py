rows_cols = int(input())

matrix = [[int(el) for el in input().split(', ')] for _ in range(rows_cols)]

primary_diagonal = []
secondary_diagonal = []

primary_sum = 0
secondary_sum = 0

idx_p = 0
idx_s = rows_cols - 1

for _ in range(rows_cols):
    primary_diagonal.append(matrix[idx_p][idx_p])
    primary_sum += matrix[idx_p][idx_p]

    secondary_diagonal.append(matrix[idx_p][idx_s])
    secondary_sum += matrix[idx_p][idx_s]

    idx_p += 1
    idx_s -= 1

print(f"Primary diagonal: {f', '.join([str(el) for el in primary_diagonal])}. Sum: {primary_sum}")
print(f"Secondary diagonal: {f', '.join([str(el) for el in secondary_diagonal])}. Sum: {secondary_sum}")
