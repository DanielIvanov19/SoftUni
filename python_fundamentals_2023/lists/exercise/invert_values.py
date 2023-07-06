num_string = input()

num_list = num_string.split(" ")
num_list = list(map(int, num_list))

for i in range(0, len(num_list)):
    num_list[i] = num_list[i] * -1
print(num_list)
# print([int(num) * -1 for num in string)