from math import ceil
natural_number = int(input())
flag = 0
if natural_number > 1:
    for i in range(2, (ceil(natural_number/2) + 1)):
        if natural_number % i == 0:
            flag = 1
            break
    if flag == 0:
        print("True")
    else:
        print("False")
else:
    print("False")