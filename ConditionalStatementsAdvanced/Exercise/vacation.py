budget = float(input())
season_type = input()

vacation_type = ''
price = 0
location = ''

if budget <= 1000 and (season_type == 'Summer' or season_type == 'Winter'):
    vacation_type = 'Camp'
    if season_type == 'Summer':
        location = 'Alaska'
        price = budget * 0.65
    elif season_type == 'Winter':
        location = 'Morocco'
        price = budget * 0.45
elif 1000 < budget <= 3000 and (season_type == 'Summer' or season_type == 'Winter'):
    vacation_type = 'Hut'
    if season_type == 'Summer':
        location = 'Alaska'
        price = budget * 0.8
    elif season_type == 'Winter':
        location = 'Morocco'
        price = budget * 0.6
else:
    vacation_type = 'Hotel'
    if season_type == 'Summer':
        location = 'Alaska'
        price = budget * 0.9
    elif season_type == 'Winter':
        location = 'Morocco'
        price = budget * 0.9

print(f'{location} - {vacation_type} - {price:.2f}')
