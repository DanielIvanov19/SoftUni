text = input()

stack_string = list(text)

while stack_string:
    removed_element = stack_string.pop()
    print(removed_element, end='')
    