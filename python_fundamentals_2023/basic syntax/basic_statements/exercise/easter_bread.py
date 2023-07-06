budget = float(input())
price_kilo_flour = float(input())
price_packet_eggs = price_kilo_flour*0.75
price_liter_milk = price_kilo_flour*1.25
needed_milk_price = price_liter_milk/4
colored_eggs = 0
breads = 0
counter = 0
minimum_price = price_packet_eggs + price_kilo_flour + needed_milk_price
while budget >= minimum_price:
    budget -= minimum_price
    breads += 1
    colored_eggs += 3
    counter += 1
    if counter == 3:
        colored_eggs = colored_eggs - (breads - 2)
        counter = 0
print(f"You made {breads} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")