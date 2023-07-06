
loading_num = int(input())


def is_loading(number):
    percent_count = number // 10
    dots_count = 10 - percent_count
    output_string = "["
    output_string += '%' * percent_count
    output_string += '.' * dots_count
    output_string += ']'
    if number != 100:
        return f"{number}% {output_string}\nStill loading..."
    else:
        return f"{number}% Complete!\n{output_string}"


result = is_loading(loading_num)
print(result)