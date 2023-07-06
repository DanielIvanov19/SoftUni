command = input()
while command != "End":
    required_sum = float(input())
    saved_money = 0
    while saved_money < required_sum:
        money = float(input())
        saved_money += money
    print(f"Going to {command}!")
    command = input()
