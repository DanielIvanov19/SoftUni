from string import ascii_letters, digits

allowed_chars = ascii_letters + digits + '-' + '_'

usernames = input().split(', ')

for username in usernames:
    if len(username) < 3 or len(username) > 16:
        continue
    temp = [char in allowed_chars for char in username]
    contains_allowed_forbidden = all(temp)

    if not contains_allowed_forbidden:
        continue

    print(username)
