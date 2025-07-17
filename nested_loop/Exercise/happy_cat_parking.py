days_count = int(input())
hours_count = int(input())

total_sum = 0

for i in range(1, days_count + 1):
    total_sum_day = 0
    for j in range(1, hours_count + 1):
        if i % 2 == 0 and j % 2 == 1:
            total_sum += 2.5
            total_sum_day += 2.5
        elif i % 2 == 1 and j % 2 == 0:
            total_sum += 1.25
            total_sum_day += 1.25
        else:
            total_sum += 1
            total_sum_day += 1
    print(f'Day: {i} - {total_sum_day:.2f} leva')
print(f'Total: {total_sum:.2f} leva')