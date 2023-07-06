hours = int(input())
mins = int (input())

first_total = hours*60 + mins
total_mins = first_total + 15

after_hours = total_mins//60
after_mins = total_mins%60

if after_hours > 23:
    after_hours = 0

if after_mins >= 0 and after_mins <= 9:
    print(f"{after_hours}:0{after_mins}")
else:
    print(f"{after_hours}:{after_mins}")