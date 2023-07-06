start_num = int(input())
end_num = int(input())

for number in range(start_num, end_num + 1):
    hun_thousands = number // 100000
    ten_thousands = (number // 10000) % 10
    thousands = (number // 1000) % 10
    hundreds = (number // 100) % 10
    tens = (number // 10) % 10
    units = number % 10

    sum_even = ten_thousands + hundreds + units
    sum_odd = hun_thousands + thousands + tens

    if sum_odd == sum_even:
        print(number, end=' ')
