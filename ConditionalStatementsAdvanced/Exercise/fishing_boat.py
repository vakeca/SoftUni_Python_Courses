budget = int(input())
season_type = input()
fisherman_count = int(input())
price = 0


if season_type == 'Spring':
    price = 3000
    if fisherman_count <= 6:
        price *= 0.9
    elif 7 <= fisherman_count <= 11:
        price *= 0.85
    elif fisherman_count >= 12:
        price *= 0.75

elif season_type == 'Summer' or season_type == 'Autumn':
    price = 4200
    if fisherman_count <= 6:
        price *= 0.9
    elif 7 <= fisherman_count <= 11:
        price *= 0.85
    elif fisherman_count >= 12:
        price *= 0.75

elif season_type == 'Winter':
    price = 2600
    if fisherman_count <= 6:
        price *= 0.9
    elif 7 <= fisherman_count <= 11:
        price *= 0.85
    elif fisherman_count >= 12:
        price *= 0.75

if fisherman_count % 2 == 0:
    if season_type != 'Autumn':
        price *= 0.95

money_left = abs(price - budget)

if budget >= price:
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    print(f'Not enough money! You need {money_left:.2f} leva.')

