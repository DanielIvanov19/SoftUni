numbers_list = [int(x) for x in input().split(", ")]

if 0 in numbers_list:
    #while numbers_list[numbers_list.index(0) + 1] != 0:
    for i in numbers_list:
        if numbers_list[i] != 0:
            continue
        numbers_list[i], numbers_list[i + 1] = numbers_list[i + 1], numbers_list[i]

print(numbers_list)