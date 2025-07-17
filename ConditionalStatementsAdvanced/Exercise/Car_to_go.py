budget = float(input())
season_type = input()

class_type = ''
car_type = ''
price = 0

if budget <= 100 and (season_type == 'Summer' or season_type == 'Winter'):
    class_type = 'Economy class'
    if season_type == 'Summer':
        car_type = 'Cabrio'
        price = budget * 0.35
    elif season_type == 'Winter':
        car_type = 'Jeep'
        price = budget * 0.65
elif 100 <= budget <= 500 and (season_type == 'Summer' or season_type == 'Winter'):
    class_type = 'Compact class'
    if season_type == 'Summer':
        car_type = 'Cabrio'
        price = budget * 0.45
    elif season_type == 'Winter':
        car_type = 'Jeep'
        price = budget * 0.80
else:
    class_type = 'Luxury class'
    car_type = 'Jeep'
    price = budget * 0.90

print(class_type)
print(f'{car_type} - {price:.2f}')


