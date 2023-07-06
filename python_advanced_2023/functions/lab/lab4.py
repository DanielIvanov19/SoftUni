my_dict = {'Peter': 21, 'George': 18, 'John': 45}
print(my_dict.items())

# sort by the key arguments in the dictionary
# we can use '-'len(x) equal to reverse = True
# we can sort by two or more arguments using (x[1], x[0])
print(sorted(my_dict.items(), key=lambda x: (x[1], -len(x[0]))))
