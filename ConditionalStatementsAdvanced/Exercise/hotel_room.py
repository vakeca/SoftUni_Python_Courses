month = input()
stay_count = int(input())

studio = 0
apartment = 0

if month == 'May' or month == 'October':
    studio = 50
    apartment = 65
    if 7 < stay_count <= 14:
        studio *= 0.95
    elif stay_count > 14:
        studio *= 0.70
        apartment *= 0.90

elif month == 'June' or month == 'September':
    studio = 75.20
    apartment = 68.70
    if stay_count > 14:
        studio *= 0.80
        apartment *= 0.90
else:
    studio = 76
    apartment = 77
    if stay_count > 14:
        apartment *= 0.90



total_studio = stay_count * studio
total_apartment = stay_count * apartment
print(f'Apartment: {total_apartment:.2f} lv.')
print(f'Studio: {total_studio:.2f} lv.')