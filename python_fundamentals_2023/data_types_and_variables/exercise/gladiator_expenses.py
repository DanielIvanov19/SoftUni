losses = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_c = 0
shield_c = 0
sword_c = 0
armor_c = 0
for i in range(1, losses + 1):
    if i % 2 == 0:
        helmet_c += 1
    if i % 3 == 0:
        sword_c += 1
    if i % 6 == 0:
        shield_c += 1
    if i % 12 == 0:
        armor_c += 1
total_price = helmet_price*helmet_c + shield_price*shield_c + sword_price * sword_c + armor_price * armor_c
print(f"Gladiator expenses: {total_price:.2f} aureus")