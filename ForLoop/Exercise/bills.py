months = int(input())

water = 20
internet = 15

total_water = 0
total_internet = 0
total_electricity = 0
total_other = 0
total_average_bills = 0

for i in range(1, months + 1):
    electricity = float(input())
    other = 0
    total_electricity += electricity
    total_water += water
    total_internet += internet
    other = (electricity + water + internet) * 0.2 + electricity + water + internet
    total_other += other

    total_average_bills = (total_electricity + total_water + total_internet + total_other) / months

print(f'Electricity: {total_electricity:.2f} lv')
print(f'Water: {total_water:.2f} lv')
print(f'Internet: {total_internet:.2f} lv')
print(f'Other: {total_other:.2f} lv')
print(f'Average: {total_average_bills:.2f} lv')
