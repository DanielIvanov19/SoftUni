num_string = input()
beggars_count = int(input())
num_list = list(map(int, num_string.split(", ")))

beggars_list = [0] * beggars_count
for idx in range(len(num_list)):
    beggar_idx = idx % beggars_count
    num = int(num_list[idx])
    beggars_list[beggar_idx] += num
print(beggars_list)
