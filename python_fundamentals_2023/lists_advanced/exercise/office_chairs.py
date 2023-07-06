number_of_rooms = int(input())
output_list = []
free_chairs = 0

for room in range(1, number_of_rooms + 1):
    user_input = input().split(' ')
    # chairs, guests_as_str = input.split()
    chairs = user_input[0]
    people = user_input[1]
    if len(chairs) >= int(people):
        free_chairs += (len(chairs) - int(people))
        continue
    else:
        difference = abs(len(chairs) - int(people))
        output_list.append(f"{difference} more chairs needed in room {room}")

if len(output_list) == 0:
    print(f"Game On, {free_chairs} free chairs left")
else:
    print('\n'.join(output_list))
