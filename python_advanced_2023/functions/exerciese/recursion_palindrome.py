def palindrome(word: str, index: int):

    if index == len(word)//2:
        return f'{word} is a palindrome'

    if word[index] != word[-index - 1]:
        return f'{word} is not a palindrome'

    return palindrome(word, index + 1)


print(palindrome('abbra', 0))

# returns where it has been called
