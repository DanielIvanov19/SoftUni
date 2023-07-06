from collections import deque


numbers = deque([int(x) for x in input().split()])

for _ in range(len(numbers)):
    print(numbers.pop(), end=' ')
