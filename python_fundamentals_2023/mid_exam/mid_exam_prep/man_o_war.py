pirate_ship = [int(x) for x in input().split('>')]
warship = [int(x) for x in input().split('>')]
max_health_capacity = int(input())
command = input()
stalemate = True
while command != "Retire":
    main_command = command.split(' ')[0]
    if main_command == "Fire":
        index_section = int(command.split(' ')[1])
        damage = int(command.split(' ')[2])
        if index_section < len(warship):
            warship[index_section] -= damage
            if warship[index_section] <= 0:
                print("You won! The enemy ship has sunken.")
                stalemate = False
                break
    if main_command == "Defend":
        start_index = int(command.split(' ')[1])
        end_index = int(command.split(' ')[2])
        damage = int(command.split(' ')[3])
        if (0 <= start_index < len(pirate_ship)) and (start_index <= end_index < len(pirate_ship)):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    stalemate = False
                    break
    if main_command == "Repair":
        index_repair = int(command.split(' ')[1])
        health_repair = int(command.split(' ')[2])
        if 0 <= index_repair < len(pirate_ship):
            if pirate_ship[index_repair] + health_repair > max_health_capacity:
                pirate_ship[index_repair] = max_health_capacity
            else:
                pirate_ship[index_repair] += health_repair
    if main_command == "Status":
        count_of_repairs = 0
        pirate_status = 0
        warship_status = 0
        for section in range(len(pirate_ship)):
            pirate_status += pirate_ship[section]
            if pirate_ship[section] < max_health_capacity / 5:
                count_of_repairs += 1
        for section in range(len(warship)):
            warship_status += warship[section]
        print(f'{count_of_repairs} sections need repair.')
    command = input()

if stalemate:
    print(f'Pirate ship status: {pirate_status}')
    print(f'Warship status: {warship_status}')
