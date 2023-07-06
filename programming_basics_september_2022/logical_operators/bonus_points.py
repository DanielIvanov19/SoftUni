num = int(input())
bonus_p = 0

if num <= 100:
    bonus_p =5
elif num > 100 and num <= 1000:
    bonus_p = num*20/100
else:
    bonus_p = num*10/100

if num % 2 == 0:
    bonus_p += 1

elif num % 5 == 0:
    bonus_p += 2

sum = num + bonus_p
print(bonus_p)
print(sum)