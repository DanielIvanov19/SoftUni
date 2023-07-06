rows_cols = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(rows_cols)]

primary_sum = 0
secondary_sum = 0

idx_p = 0
idx_s = rows_cols - 1

for _ in range(rows_cols):
    primary_sum += matrix[idx_p][idx_p]
    secondary_sum += matrix[idx_p][idx_s]

    idx_p += 1
    idx_s -= 1

difference = abs(primary_sum - secondary_sum)
print(difference)
