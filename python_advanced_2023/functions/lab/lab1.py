def sum_nums(**kwargs):
    for key, value in kwargs.items():
        print(f'The key is: {key} and the value is: {value}')
    return kwargs


print(sum_nums(b=5, a=7))
