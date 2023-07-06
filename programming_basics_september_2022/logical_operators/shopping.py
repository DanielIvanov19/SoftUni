budget = float(input())
amount_graphic_cards = int(input())
amount_processors = int(input())
amount_ram = int(input())

graphics_price = 250
processor_price = (amount_graphic_cards*graphics_price)*0.35
ram_price = (amount_graphic_cards*graphics_price)*0.1

total = amount_graphic_cards*graphics_price + processor_price*amount_processors + ram_price*amount_ram
if amount_graphic_cards > amount_processors:
    final_price = total*0.85
else:
    final_price = total

difference = abs(budget - final_price)

if budget >= total:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")