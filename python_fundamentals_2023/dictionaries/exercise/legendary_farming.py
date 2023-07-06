special_material = {
    'shards': 0,
    'fragments': 0,
    'motes': 0
}
legendary_item_material = {
    'shards': "Shadowmourne",
    'fragments': "Valanyr",
    'motes': "Dragonwrath"
}

junk_materials = {}
crafted = False
while not crafted:
    line = input()
    materials = line.split()

    for idx in range(0, len(materials) - 1, 2):
        quantity = int(materials[idx]) # num
        material = materials[idx + 1].lower() # material

        if material in special_material:
            special_material[material] += quantity
            if special_material[material] >= 250:
                special_material[material] -= 250
                crafted = True
                print(f"{legendary_item_material[material]} obtained!")
                break
        else:
            if material in junk_materials:
                junk_materials[material] += quantity
            else:
                junk_materials[material] = quantity

for material, count in special_material.items():
    print(f'{material}: {count}')

for material, count in junk_materials.items():
    print(f'{material}: {count}')
    