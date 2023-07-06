import math

c_tournaments = int(input())
init_points = int(input())
final_points = init_points
win_counter = 0
for _ in range(1, c_tournaments + 1):
    stage = input()
    if stage.upper() == "W":
        final_points += 2000
        win_counter += 1
    elif stage.upper() == "F":
        final_points += 1200
    elif stage.upper() == "SF":
        final_points += 720

average = math.floor((final_points - init_points) / c_tournaments)
win_percentage = win_counter / c_tournaments * 100
print(f"Final points: {final_points}")
print(f"Average points: {average}")
print(f"{win_percentage:.2f}%")
