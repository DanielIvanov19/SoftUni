from collections import deque


tools = deque([int(x) for x in input().split()])
substances = deque([int(x) for x in input().split()])
challenges = deque([int(x) for x in input().split()])

while True:
    tool = tools.popleft()
    substance = substances.pop()

    multiplied = tool * substance
    for challenge in challenges:
        if multiplied == challenge:
            challenges.remove(challenge)
            # tools.remove(tool)
            # substances.remove(substance)
            break
    else:
        tool += 1
        tools.append(tool)
        substance -= 1
        if substance >= 1:
            substances.append(substance)

    if not challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        if tools:
            print(f"Tools: {', '.join([str(tool) for tool in tools])}")
        if substances:
            print(f"Substances: {', '.join([str(substance) for substance in substances])}")
        break
    if not substances or not challenges:
        print("Harry is lost in the temple. Oblivion awaits him.")
        if tools:
            print(f"Tools: {', '.join([str(tool) for tool in tools])}")
        if substances:
            print(f"Substances: {', '.join([str(substance) for substance in substances])}")
        if challenges:
            print(f"Challenges: {', '.join([str(challenge) for challenge in challenges])}")
        break

