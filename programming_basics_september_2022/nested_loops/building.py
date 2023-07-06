floors = int(input())
rooms = int(input())

flat_num_c = 0
type_of_flat = ''


for f in range(floors, 0, -1):
    for r in range(rooms):
        flat_num = f * 10 + r

        if f == floors:
            type_of_flat = f"L{flat_num}"
        elif f % 2 == 0:
            type_of_flat = f"O{flat_num}"
        elif f % 2 != 0:
            type_of_flat = f"A{flat_num}"
        print(type_of_flat, end=' ')
    print()