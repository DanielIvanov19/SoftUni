from collections import deque

kids_queue = deque(input().split())

nth_kid = int(input()) - 1

while len(kids_queue) > 1:
    #for _ in range(nth_kid):
        # can use the .rotate() method
        # negative to move to end / positive to move to start
        #kids_queue.append(kids_queue.popleft())
    kids_queue.rotate(-nth_kid)
    print(f'Removed {kids_queue.popleft()}')

print(f"Last is {kids_queue.popleft()}")


