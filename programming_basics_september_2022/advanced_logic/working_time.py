hour = int(input())
day_of_week = input()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if 9 < hour < 19:
    if day_of_week in days:
        print("open")
    else:
        print("closed")
else:
    print("closed")