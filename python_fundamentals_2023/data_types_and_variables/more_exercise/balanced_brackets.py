lines = int(input())
message = ""
balanced = True
for i in range(1, lines + 1):
    character = input()
    message += character
for k in range(0, len(message)):
    if message[k] == ")" and not message[0:k].__contains__('('):
        balanced = False
        print("UNBALANCED")
        break

message.index("(")
