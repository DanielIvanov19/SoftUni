capital_index = input()
index_list = []
for i in range(0, len(capital_index)):
    if capital_index[i] == capital_index[i].upper():
        index_list.append(i)
print(index_list)