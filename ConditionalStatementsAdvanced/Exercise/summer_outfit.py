degree = int(input())
time_of_day = input()
Outfit = ''
Shoes = ''

if 10 <= degree <=18:
    if time_of_day == 'Morning':
        Outfit = 'Sweatshirt'
        Shoes = 'Sneakers'
    elif time_of_day == 'Afternoon' or time_of_day == 'Evening':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
elif 18 < degree <= 24:
    if time_of_day == 'Morning' or time_of_day == 'Evening':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    elif time_of_day == 'Afternoon':
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
elif degree >= 25:
    if time_of_day == 'Morning':
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
    elif time_of_day == 'Afternoon':
        Outfit = 'Swim Suit'
        Shoes = 'Barefoot'
    elif time_of_day == 'Evening':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'

print(f"It's {degree} degrees, get your {Outfit} and {Shoes}.")
