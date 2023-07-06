from collections import deque

starting_quantity = int(input())

water_queue = deque()

while True:
    name = input()
    if name == "Start":
        break
    water_queue.append(name)

while True:
    command = input()
    if command == "End":
        break

    elif len(command) == 1:
        if starting_quantity >= int(command):
            if water_queue:
                starting_quantity = starting_quantity - int(command)
                received = water_queue.popleft()
                print(f"{received} got water")
        else:
            if water_queue:
                not_received = water_queue.popleft()
                print(f'{not_received} must wait')

    elif command.split()[0] == 'refill':
        starting_quantity = starting_quantity + int(command.split()[1])

print(f"{starting_quantity} liters left")
