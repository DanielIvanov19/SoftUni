ex_list = [100, 105, 300]
my_dict = {index: ("even" if index % 2 == 0 else "odd") for index, el in enumerate(ex_list) }

# for index, el in enumerate(ex_list):
    # my_dict[index] = el
print(my_dict)