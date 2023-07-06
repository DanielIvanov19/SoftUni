start_interval = int(input())
end_interval = int(input())
flag = False
magic_num = int(input())

combination_counter = 0

for i in range(start_interval, end_interval + 1):
    for z in range(start_interval, end_interval + 1):
        combination_counter += 1

        if i + z == magic_num:
            print(f"Combination N:{combination_counter} ({z} + {i} = {magic_num})")
            flag = True
            break
    if flag:
        break
if not flag:
    print(f"{combination_counter} combinations - neither equals {magic_num}")