num = int(input())
counter = 1
current_num = 1
for row in range(1, num + 1):

    for i in range(1, row + 1):
        print(current_num, end=' ')
        counter += 1
        if counter > num:
            break

        current_num += 1
    print()

    if counter > num:
        break
