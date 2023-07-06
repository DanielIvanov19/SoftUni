class ValueCannotBeNegative(Exception):
    pass


for num in range(5):
    try:
        number = int(input())
        if num < 0:
            raise ValueCannotBeNegative
    except ValueError:
        print('Not a valid number. Continue to next one')
     