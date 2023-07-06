year_input = int(input())
digits = ...
is_distinct = False
while not is_distinct:
    visited = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    num = year_input
    while num != 0:
        if visited[num % 10] == 1:
            break
        visited[num % 10] = 1
        num = int(num / 10)
    if num == 0:
        print(num)
        is_distinct = True
        break
    else:
        year_input += 1
