from collections import deque


clothes = deque([int(x) for x in input().split()])
rack_capacity = int(input())

racks_c = 1
current_rack_space = rack_capacity

while clothes:
    cloth = clothes.pop()

    if current_rack_space >= cloth:
        current_rack_space -= cloth
    else:
        racks_c += 1
        current_rack_space = rack_capacity - cloth
print(racks_c)
