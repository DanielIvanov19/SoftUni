
n = int(input())
for _ in range(0, n):
    word = input()
    if word.__contains__(",") or word.__contains__(".") or word.__contains__("_"):
        print(f"{word} is not pure!")
    else:
        print(f"{word} is pure.")

for _ in range(n):
    word = input()
    is_pure = True

    for ch in word:
        if ch == ',' or ch == '_' or ch == '.':
            break
    if is_pure:
        print("pure")
    else:
        print("not pure")
