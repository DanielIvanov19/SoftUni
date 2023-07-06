num_cars = int(input())

cars = {}
for _ in range(num_cars):
    car = input()
    car_name = car.split('|')[0]
    car_specs = [int(car.split('|')[1]), int(car.split('|')[2])]
    cars[car_name] = car_specs

while True:
    command = input()
    if command == "Stop":
        for el in cars:
            print(f"{el} -> Mileage: {cars[el][0]} kms, Fuel in the tank: {cars[el][1]} lt.")
        break
    elif command.split(" : ")[0] == "Drive":
        car_command = command.split(' : ')[1]
        desired_distance = int(command.split(' : ')[2])
        needed_fuel = int(command.split(' : ')[3])

        current_mileage = cars[car_command][0]
        current_fuel = cars[car_command][1]
        if needed_fuel <= current_fuel:
            current_fuel -= needed_fuel
            current_mileage += desired_distance
            cars[car_command][0] = current_mileage
            cars[car_command][1] = current_fuel
            print(f"{car_command} driven for {desired_distance} kilometers. {needed_fuel} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")
        if current_mileage >= 100000:
            del cars[car_command]
            print(f"Time to sell the {car_command}!")

    elif command.split(" : ")[0] == "Refuel":
        car_command = command.split(' : ')[1]
        refuel = int(command.split(' : ')[2])

        current_mileage = cars[car_command][0]
        current_fuel = cars[car_command][1]

        if current_fuel + refuel > 75:
            difference = 75 - current_fuel
            new_fuel = 75
            cars[car_command][1] = new_fuel
            print(f"{car_command} refueled with {difference} liters")
        else:
            cars[car_command][1] += refuel
            print(f"{car_command} refueled with {refuel} liters")

    elif command.split(" : ")[0] == "Revert":
        car_command = command.split(' : ')[1]
        revert = int(command.split(' : ')[2])

        current_mileage = cars[car_command][0]

        after_revert = current_mileage - revert

        if after_revert < 10000:
            cars[car_command][0] = 10000
        else:
            cars[car_command][0] = after_revert
            print(f"{car_command} mileage decreased by {revert} kilometers")
