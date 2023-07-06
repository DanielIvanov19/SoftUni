capacity = 255
init_liters = 0
times_pour = int(input())
for _ in range(0, times_pour):
    liters = int(input())
    if init_liters + liters <= capacity:
        init_liters += liters
    else:
        print("Insufficient capacity!")
        continue
print(init_liters)