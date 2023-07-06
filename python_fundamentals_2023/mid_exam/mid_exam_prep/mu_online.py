init_health = 100
bitcoins = 0

dungeon_rooms = input().split('|')
is_managed = True
for room in range(len(dungeon_rooms)):
    best_room = room + 1
    command = dungeon_rooms[room].split(' ')[0]
    number = int(dungeon_rooms[room].split(' ')[1])
    if command == "potion":
        after_heal = init_health + number
        if after_heal > 100:
            change = 100 - init_health
            init_health = 100
            print(f"You healed for {change} hp.")
            print(f"Current health: {init_health} hp.")
        else:
            init_health = after_heal
            print(f"You healed for {number} hp.")
            print(f"Current health: {init_health} hp.")
    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        damage = init_health - number
        if damage > 0:
            print(f"You slayed {command}.")
            init_health -= number
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {best_room}")
            is_managed = False
            break

if is_managed:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {init_health}")
