init_list = input().split('!')

command = ''

while command != 'Go Shopping!':
    command = input()
    if command.split(' ')[0] == "Urgent":
        urgent_item = command.split(' ')[1]
        if urgent_item not in init_list:
            init_list.insert(0, urgent_item)
        else:
            continue
    if command.split(' ')[0] == "Unnecessary":
        unnecessary_item = command.split(' ')[1]
        if unnecessary_item in init_list:
            init_list.remove(unnecessary_item)
        else:
            continue
    if command.split(' ')[0] == "Correct":
        old_name = command.split(' ')[1]
        new_name = command.split(' ')[2]
        if old_name == new_name:
            continue
        else:
            if old_name in init_list:
                index_old = init_list.index(old_name)
                init_list.remove(old_name)
                init_list.insert(index_old, new_name)
            else:
                continue
    if command.split(' ')[0] == "Rearrange":
        rearranged = command.split(' ')[1]
        if rearranged in init_list:
            init_list.remove(rearranged)
            init_list.append(rearranged)
        else:
            continue

print(', '.join(init_list))