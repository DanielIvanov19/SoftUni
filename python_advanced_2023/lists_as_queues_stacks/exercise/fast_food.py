from collections import deque


food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

for order in orders.copy():
    if food - order >= 0:
        orders.popleft()
        food -= order
    else:
        print(f"Orders left: {' '.join([str(x) for x in orders])}")
        break
        # if we reach the break -> won't reach the last else
else:
    print("Orders complete")
