license_plate_user = {}

count = int(input())

for _ in range(count):
    command_args = input().split()
    command = command_args[0]
    name = command_args[1]

    if command == 'register':
        license_plate = command_args[2]
        if name in license_plate_user:
            print(f"ERROR: already registered with plate number {license_plate_user[name]}")
        else:
            license_plate_user[name] = license_plate
            print(f"{name} registered {license_plate} successfully")
    else:
        if name in license_plate_user:
            license_plate_user.pop(name)
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

for user in license_plate_user:
    print(f"{user} => {license_plate_user[user]}")

