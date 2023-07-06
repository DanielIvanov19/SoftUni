user_input = input()

vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']

compr_input = ''.join([x for x in user_input if x not in vowels])
print(compr_input)
