deposit = float(input())
deadline = int(input())
annual_rate = float(input())
rate_per_year = deposit*(annual_rate/100)
rate_per_month = rate_per_year/12
total_sum = deposit + (rate_per_month * deadline)
print(total_sum)
