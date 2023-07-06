command = input()
first_num = int(input())
second_num = int(input())


def calculate(command, first_num, second_num):
    if command == "multiply":
        result = first_num * second_num
        return result
    elif command == "divide":
        result = first_num // second_num
        return result
    elif command == "add":
        result = first_num + second_num
        return result
    elif command == "subtract":
        result = first_num - second_num
        return result


print(calculate(command, first_num, second_num))