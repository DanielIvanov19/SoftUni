from collections import deque

# import time
customers = deque()

# start_time = time.time()

while True:
    line = input()
    if line == "End":
        break
    elif line == 'Paid':
        while customers:
            print(customers.popleft())
    else:
        customers.append(line)
# diff = time.time() - start_time
print(f"{len(customers)} people remaining.")
# print(diff)
