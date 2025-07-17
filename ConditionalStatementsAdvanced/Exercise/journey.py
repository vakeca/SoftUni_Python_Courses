budget = float(input())
season_type = input()

destination = ''
vacation_type = ''
total_sum = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season_type == 'summer':
        total_sum = budget * 0.3
        vacation_type = 'Camp'
    elif season_type == 'winter':
        total_sum = budget * 0.7
        vacation_type = 'Hotel'
elif 100 <= budget <= 1000:
    destination = 'Balkans'
    if season_type == 'summer':
        total_sum = budget * 0.4
        vacation_type = 'Camp'
    elif season_type == 'winter':
        total_sum = budget * 0.8
        vacation_type = 'Hotel'
elif budget > 1000:
    destination = 'Europe'
    vacation_type = 'Hotel'
    total_sum = budget * 0.9


print(f'Somewhere in {destination}')
print(f'{vacation_type} - {total_sum:.2f}')




