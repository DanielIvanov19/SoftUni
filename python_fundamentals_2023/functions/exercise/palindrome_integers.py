list_numbers = [int(x) for x in input().split(", ")]


def is_palindrome(numbers):
    for number in numbers:
        palindrome = ""
        num_to_string = str(number)
        palindrome = num_to_string[::-1]
        if num_to_string == palindrome:
            print("True")
        else:
            print("False")


is_palindrome(list_numbers)
