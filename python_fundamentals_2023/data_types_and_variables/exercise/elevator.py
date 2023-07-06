from math import ceil
num_people = int(input())
capacity = int(input())
courses = 0
while num_people >= capacity:
    num_people -= capacity
    courses += 1
if num_people == 0:
    print(courses)
else:
    print(courses + 1)

print(ceil(num_people/capacity))