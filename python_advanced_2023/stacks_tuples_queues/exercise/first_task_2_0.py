first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())

functions = {
    "Add First": lambda x: [first.add(int(el)) for el in x],
    "Add Second": lambda x: [second.add(int(el)) for el in data],
    "Remove First": lambda x: [first.discard(int(el)) for el in data],
    "Remove Second": lambda x: [second.discard(int(el)) for el in data],
    "Check Subset": lambda x: print(first.issubset(second) or second.issubset(first))
}

for _ in range(int(input())):
    first_command, second_command, *data = input().split()

    command = first_command + " " + second_command

    functions[command]([int(x) for x in data])

print(*sorted(first), sep=', ')
print(*sorted(second), sep=', ')
