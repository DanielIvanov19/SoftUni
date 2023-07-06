stack_parenthesis = []
text = input()

for index in range(len(text)):
    if text[index] == '(':
        stack_parenthesis.append(index)
    elif text[index] == ')':
        start_pos = stack_parenthesis.pop()
        end_pos = index + 1
        print(text[start_pos:end_pos])