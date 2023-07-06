# if we use * or ** in the definition of the function we pack
# if we use * or ** when we call the function we unpack
# GitHub/InesIvanova
def nums(a, b, c):
    return a + b + c


def some_func(name, age):
    print(f'{name} is {age} years old')


person = {'age' : 20, 'name' : 'Peter', 'asd' : 5}

some_func(**person)


my_nums = [1, 2, 3]
print(nums(*my_nums))
