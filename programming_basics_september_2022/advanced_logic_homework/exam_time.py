exam_hour = int(input())
exam_min = int(input())
arrive_hour = int(input())
arrive_min = int(input())
exam_total = exam_hour * 60 + exam_min
student_total = arrive_hour * 60 + arrive_min
difference = exam_total - student_total

if arrive_hour == exam_hour and arrive_min == exam_min:
    print("On time")
elif difference == 0 or 0 < difference <= 30:
    print("On time")
    print(f"{difference} minutes before the start")
elif difference > 30:
    print("Early")
    if difference > 59:
        dif_hours = difference // 60
        dif_min = difference % 60
        if dif_min < 10:
            print(f"{dif_hours}:0{dif_min} hours before the start")
        else:
            print(f"{dif_hours}:{dif_min} hours before the start")
    else:
        print(f"{abs(difference)} minutes before the start")
elif difference < 0:
    print("Late")
    if abs(difference) > 59:
        dif_hours = abs(difference) // 60
        dif_min = abs(difference) % 60
        if dif_min < 10:
            print(f"{dif_hours}:0{dif_min} hours after the start")
        else:
            print(f"{dif_hours}:{dif_min} hours after the start")
    else:
        print(f"{abs(difference)} minutes after the start")
