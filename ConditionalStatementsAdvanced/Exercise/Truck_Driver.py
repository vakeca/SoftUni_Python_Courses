season_type = input()
km_per_month = float(input())

price_per_km = 0

if km_per_month <= 5000:
    if season_type == 'Spring' or season_type == 'Autumn':
        price_per_km = km_per_month * 0.75 * 4
    elif season_type == 'Summer':
        price_per_km = km_per_month * 0.90 * 4
    else:
        price_per_km = km_per_month * 1.05 * 4
elif 5000 < km_per_month <= 10000:
    if season_type == 'Spring' or season_type == 'Autumn':
        price_per_km = km_per_month * 0.95 * 4
    elif season_type == 'Summer':
        price_per_km = km_per_month * 1.10 * 4
    else:
        price_per_km = km_per_month * 1.25 * 4
else:
    if season_type == 'Spring' or season_type == 'Autumn':
        price_per_km = km_per_month * 1.45 * 4
    elif season_type == 'Summer':
        price_per_km = km_per_month * 1.45 * 4
    else:
        price_per_km = km_per_month * 1.45 * 4

total_salary = price_per_km - price_per_km * 0.10

print(f'{total_salary:.2f}')



