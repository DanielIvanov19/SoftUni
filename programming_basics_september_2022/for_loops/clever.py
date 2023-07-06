age = int(input())
price_washing_machine = float(input())
price_toy = int(input())
b_toy = 0
start_sum = 0
budget = 0
bro_count = 0
for i in range(1, age + 1):
    if i % 2 != 0:
        b_toy += 1
    else:
        bro_count += 1
        start_sum += 10
        budget += start_sum
result = (b_toy * price_toy) + budget - bro_count * 1
diff = abs(result - price_washing_machine)
if result >= price_washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
