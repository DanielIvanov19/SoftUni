my_stack = [5, 6, 7, 8, 9, 10, 11]

while len(my_stack) > 1:
    removed = my_stack.pop()
    print(removed)
    print(my_stack)

print(f"Last element is {my_stack[-1]}")
