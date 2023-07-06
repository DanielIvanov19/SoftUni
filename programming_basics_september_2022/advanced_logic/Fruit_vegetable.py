product = input()

fruits = ["banana", "apple", "kiwi", "lemon", "grapes"]
vegetables = ["tomato", "cucumber", "pepper", "carrot"]

if product in fruits:
    print("fruit")
elif product in vegetables:
    print("vegetable")
else:
    print("unknown")