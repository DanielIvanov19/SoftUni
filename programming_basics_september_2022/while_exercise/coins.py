change = float(input())
change_st = change * 100
c_coins = 0
while change_st > 0:
    if change_st >= 200:
        change_st -= 200
    elif change_st >= 100:
        change_st -= 100
    elif change_st >= 50:
        change_st -= 50
    elif change_st >= 20:
        change_st -= 20
    elif change_st >= 10:
        change_st -= 10
    elif change_st >= 5:
        change_st -= 5
    elif change_st >= 2:
        change_st -= 2
    elif change_st >= 1:
        change_st -= 1
    else:
        break

    c_coins += 1


print(c_coins)