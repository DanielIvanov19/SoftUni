first_time = int(input())
second_time = int(input())
third_time = int(input())

total_time = first_time+second_time+third_time
minutes = total_time//60
seconds = total_time%60

if  seconds >= 0 and seconds <= 9:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")