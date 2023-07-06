hidden_message = input()

numbers_list = []
non_numbers_list = []

take_list = []
skip_list = []

final_message = ''

for item in range(len(hidden_message)):
    if hidden_message[item].isdigit():
        number = int(hidden_message[item])
        numbers_list.append(number)
for num in numbers_list:
    hidden_message = hidden_message.replace(str(num), '')
for i in range(len(numbers_list)):
    if i % 2 == 0:
        take_list.append(numbers_list[i])
    else:
        skip_list.append(numbers_list[i])
index_pos = 0
for i in range(len(take_list)):
    read_index = take_list[i]
    skip_index = skip_list[i]

    if read_index == 0:
        if skip_index == 0:
            continue
        else:
            index_pos += read_index
    else:
        read_chars = read_index
        for non_num in range(index_pos, index_pos + read_index):
            if non_num > len(hidden_message) - 1:
                break
            final_message += hidden_message[non_num]
        index_pos += skip_index + read_chars
print(final_message)
