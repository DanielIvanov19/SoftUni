password = input()


def length_is_valid(password_check):
    length = len(password_check)
    if 6 <= length <= 10:
        return True
    else:
        return False


def contains_all_numbers(password_check):
    return password_check.isalnum()


def contains_at_least_two_digits(password_check):
    digits_c = 0
    for ch in password_check:
        if ch.isdigit():
            digits_c += 1
    return digits_c >= 2


is_valid = True

if not length_is_valid(password):
    is_valid = False
    print('Password must be between 6 and 10 characters')
if not contains_all_numbers(password):
    is_valid = False
    print('Password must consist only of letters and digits')
if not contains_at_least_two_digits(password):
    is_valid = False
    print('Password must have at least 2 digits')
if is_valid:
    print('Password is valid')


# anotha one

def validate_password(password_check):
    errors = []
    if not length_is_valid(password):
        errors.append('Password must be between 6 and 10 characters')
    if not contains_all_numbers(password):
        errors.append('Password must consist only of letters and digits')
    if not contains_at_least_two_digits(password):
        errors.append('Password must have at least 2 digits')
    return errors


errors = validate_password(password)
if len(errors):
    for error in errors:
        print(error)
else:
    print('Password is valid')
