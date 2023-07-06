firstNum = int(input())
secondNum = int(input())
thirdNum = int(input())


def smallest_number(first_num, second_num, third_num):
    smallest = min(first_num, second_num, third_num)
    return smallest


print(smallest_number(firstNum, secondNum, thirdNum))
