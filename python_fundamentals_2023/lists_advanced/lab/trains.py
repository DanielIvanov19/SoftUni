length = int(input())

train = [0] * length

command = input()
while command != 'End':
    #  split_data = command.split()
    #  action = split_data = split_data[0]
    action = command.split()[0]
    if action == 'add':
        n_people = int(command.split()[1])
        train[-1] += n_people
    elif action == 'insert':
        index = int(command.split()[1])
        n_people = int(command.split()[2])
        train[index] += n_people
    elif action == 'leave':
        index = int(command.split()[1])
        n_people = int(command.split()[2])
        train[index] -= n_people
    command = input()

print(train)
