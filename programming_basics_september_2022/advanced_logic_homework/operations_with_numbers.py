n1 = int(input())
n2 = int(input())

operator = input()

if operator == "+":
    result = n1 + n2
    if result % 2 == 0:
        num_type = "even"
    else:
        num_type = "odd"
    print(f"{n1} {operator} {n2} = {result} - {num_type}")
elif operator == "-":
    result = n1 - n2
    if result % 2 == 0:
        num_type = "even"
    else:
        num_type = "odd"
    print(f"{n1} {operator} {n2} = {result} - {num_type}")
elif operator == "*":
    result = n1 * n2
    if result % 2 == 0:
        num_type = "even"
    else:
        num_type = "odd"
    print(f"{n1} {operator} {n2} = {result} - {num_type}")
elif operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 / n2
        print(f"{n1} {operator} {n2} = {result}")

elif operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 % n2
        print(f"{n1} {operator} {n2} = {result}")
