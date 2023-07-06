#for i in range(12):
#    if i % 2 == 0:
#        continue
#    print(i)

import random

user_input = int(input('Enter the num between 1 and 3: '))
guess_num = random.randint(1, 3)

if user_input == guess_num:
    print('Successful guess!')
else:
    print('Better luck next time!')