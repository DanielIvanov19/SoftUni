from collections import deque

green_light_duration = int(input())
free_window = int(input())

cars = deque()
total_cars = 0

car_info = input()

while car_info != "END":
    if car_info != "green":
        cars.append(car_info)
    else:
        current_green = green_light_duration

        while current_green > 0 and cars:
            car = cars.popleft()
            time = current_green + free_window

            if len(car) > time:
                print(f"A crash happened!\n{car} was hit at {car[time]}.")
                raise SystemExit

            current_green -= len(car)
            total_cars += 1
    car_info = input()

print(f"Everyone is safe.\n{total_cars} total cars passed the crossroads.")
