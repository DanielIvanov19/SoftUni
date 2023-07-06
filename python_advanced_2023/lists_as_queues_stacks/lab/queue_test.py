import time
from collections import deque

list_queue = [el for el in range(1, 100000)]
queue = deque(list_queue)

start_time = time.time()

while list_queue:
    list_queue.pop(0)

diff = time.time() - start_time
print(f'as list: {diff}')

start_time = time.time()
while queue:
    queue.popleft()

diff = time.time() - start_time
print(f'as queue: {diff}')
