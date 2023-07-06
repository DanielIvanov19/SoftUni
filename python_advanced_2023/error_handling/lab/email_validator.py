from re import findall


class NameTooShort(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbol(Exception):
    pass


class InvalidNameError(Exception):
    pass


MIN_EMAIL_LENGTH = 4
valid_domains = ['.com', '.bg', '.org', '.net']
pattern_name = r'\w+'
pattern_domain = r'\.[a-z]+'

email = input()

while email != 'End':
    if email.count('@') > 1:
        raise MoreThanOneAtSymbol("Email must contain only one '@' symbol!")

    if len(email.split('@')[0]) < MIN_EMAIL_LENGTH:
        raise NameTooShort('Name must be more than 4 characters!')

    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain '@' symbol!")

    if findall(pattern_name, email)[0] != email.split('@')[0]:
        raise InvalidNameError('Name can contain only letters, digits and underscores!')

    if findall(pattern_domain, email)[-1] not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print('Email is valid')

    email = input()