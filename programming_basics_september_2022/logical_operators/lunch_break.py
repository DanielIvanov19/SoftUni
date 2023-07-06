import math

series_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration/8
free_time = break_duration/4

spare_time = break_duration-(lunch_time+free_time)

difference = abs(spare_time-episode_duration)

if spare_time >= episode_duration:
    print(f"You have enough time to watch {series_name} and left with {math.ceil(difference)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {math.ceil(difference)} more minutes.")
