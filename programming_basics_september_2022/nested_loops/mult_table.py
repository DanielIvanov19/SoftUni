flag = False

for fnum in range (1, 11):
    for snum in range (1, 11):
        res = fnum * snum
        print(res)
        if fnum == 1:
            flag = True
            break
    if flag:
        break