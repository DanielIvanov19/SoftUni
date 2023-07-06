text = input()

# emojis = text.split(':')
# for emoji in emojis[1:]:
#    if emoji:
#        symbol = emoji[0]
#        print(f':{symbol}')

for idx in range(len(text)):
    ch = text[idx]
    if ch == ':' and idx + 1 < len(text):
        symbol = text[idx + 1]
        print(f':{symbol}')
        idx += 1