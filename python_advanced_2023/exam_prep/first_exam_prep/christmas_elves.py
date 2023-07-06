from collections import deque

elves = deque([int(x) for x in input().split()])
materials = deque([int(x) for x in input().split()])

total_energy = 0
total_toys = 0
iterations = 0

while elves and materials:
    current_elf = elves.popleft()
    current_material = materials[-1]

    if current_elf < 5:
        continue
    iterations += 1
    current_toys_made = 0

    if iterations % 3 == 0:
        current_material *= 2
        current_toys_made += 1

    if current_elf >= current_material:
        total_energy += current_material
        current_elf -= current_material
        if iterations % 5 != 0:
            current_elf += 1
            current_toys_made += 1
        else:
            current_toys_made = 0
            #  current_elf -= 1
        materials.pop()

    else:
        current_elf *= 2
        current_toys_made = 0

    total_toys += current_toys_made

    elves.append(current_elf)

print(f'Toys: {total_toys}')
print(f'Energy: {total_energy}')
if elves:
    print(f"Elves left: {', '.join(str(x) for x in elves)}")
if materials:
    print(f"Boxes left: {', '.join(str(x) for x in materials)}")
