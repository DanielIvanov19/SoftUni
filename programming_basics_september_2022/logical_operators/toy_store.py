trip_price = float(input())
puzzle_count = int(input())
dolls_count = int(input())
teddy_count = int(input())
minion_count = int(input())
truck_count = int(input())

total_sum = (puzzle_count*2.6 + dolls_count*3 + teddy_count*4.1 + minion_count*8.2 + truck_count*2)

total_count = puzzle_count + dolls_count + teddy_count + minion_count + truck_count
if total_count >= 50:
    discount_price = total_sum*0.75
    profit = discount_price - discount_price*0.1
else:
    profit = total_sum*0.9

if profit >= trip_price:
    left = profit-trip_price
    print(f"Yes! {left:.2f} lv. left.")
else:
    needed = trip_price - profit
    print(f"No! {needed:.2f} lv. needed.")
