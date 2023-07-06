words_keys = [el.lower() for el in input().split()]
default = 0

occurencies = dict.fromkeys(words_keys, default)

for word in words_keys:
    occurencies[word] = words_keys.count(word)
for word, count in occurencies.items():
    if count % 2 != 0:
        print(word, end=' ')
