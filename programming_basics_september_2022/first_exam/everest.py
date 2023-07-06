start_height = 5364
goal = 8848
days = 1
command = input()
while command != "END":
    if command == "Yes":
        days += 1
        if days > 5:
            break
        meters = int(input())
        start_height += meters
        if start_height >= goal:
            break
    elif command == "No":
        meters = int(input())
        start_height += meters
        if start_height >= goal:
            break
    command = input()
if start_height >= goal:
    print(f"Goal reached for {days} days!")
else:
    print("Failed!")
    print(start_height)
