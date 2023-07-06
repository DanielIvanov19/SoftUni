tribonacci_number = int(input())


def tribonacci_ouput(tribonacci_num):
    trib_list = [1]
    for i in range(0, tribonacci_num - 1):
        sum_t = 0
        if i < 2:
            for el in trib_list:
                sum_t += el
            trib_list.append(sum_t)
        else:
            index_t = i - 2
            sum_t = sum(trib_list[index_t:])
            trib_list.append(sum_t)

    str_trib_list = map(str, trib_list)
    return ' '.join(str_trib_list)


result = tribonacci_ouput(tribonacci_number)

print(result)

