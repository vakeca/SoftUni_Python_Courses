deposit_sum = float(input())
month_deadline = int(input())
year_rate = float(input())
year_percent = year_rate / 100
sum_percent = deposit_sum * year_percent
month_percent = sum_percent / 12

total_sum = deposit_sum + month_deadline * month_percent
print(total_sum)