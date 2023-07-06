import math

record = float(input())
meters = float(input())
meters_per_sec = float(input())

delay = math.floor(meters/15)*12.5
attempt_time = meters*meters_per_sec + delay

if attempt_time < record:
    print(f"Yes, he succeeded! The new world record is {attempt_time:.2f}.")
else:
    print(f"No, he failed! He was {(attempt_time-record):.2f} seconds slower.")

