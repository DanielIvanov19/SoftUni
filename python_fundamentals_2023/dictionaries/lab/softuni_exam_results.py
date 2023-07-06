


while True:
    line = input()
    if line == "exam finished":
        break
    args = input().split('-')
    if args[1] == "banned":
        username = args[0]

    else:
        username = args[0]
        language = args[1]
        points = args[2]


