hriz_count = int(input())
roses_count = int(input())
tulip_count = int(input())
season_type = input()
holiday_or_no = input()

arrange = 2
hriz_price = 0
roses_price = 0
tulip_price = 0

total_hriz_price = hriz_count * hriz_price
total_roses_price = roses_count * roses_price
total_tulip_price = tulip_count * tulip_price
bucket_price = total_hriz_price + total_roses_price + total_tulip_price

bucket = hriz_count + roses_count + tulip_count

if holiday_or_no == 'Y' and (season_type == 'Spring' or season_type == 'Summer'):
    hriz_price = 2
    roses_price = 4.10
    tulip_price = 2.50
    hriz_price += hriz_price * 0.15
    roses_price += roses_price * 0.15
    tulip_price += tulip_price * 0.15
    total_hriz_price = hriz_count * hriz_price
    total_roses_price = roses_count * roses_price
    total_tulip_price = tulip_count * tulip_price
    bucket_price = total_hriz_price + total_roses_price + total_tulip_price
    if season_type == 'Spring' and tulip_count > 7:
        bucket_price = bucket_price - bucket_price * 0.05
elif holiday_or_no == 'N' and (season_type == 'Spring' or season_type == 'Summer'):
    hriz_price = 2
    roses_price = 4.10
    tulip_price = 2.50
    total_hriz_price = hriz_count * hriz_price
    total_roses_price = roses_count * roses_price
    total_tulip_price = tulip_count * tulip_price
    bucket_price = total_hriz_price + total_roses_price + total_tulip_price
    if season_type == 'Spring' and tulip_count > 7:
        bucket_price = bucket_price - bucket_price * 0.05
elif holiday_or_no == 'N' and (season_type == 'Autumn' or season_type == 'Winter'):
    hriz_price = 3.75
    roses_price = 4.50
    tulip_price = 4.15
    total_hriz_price = hriz_count * hriz_price
    total_roses_price = roses_count * roses_price
    total_tulip_price = tulip_count * tulip_price
    bucket_price = total_hriz_price + total_roses_price + total_tulip_price
    if season_type == 'Winter' and roses_count >= 10:
        bucket_price *= 0.90
elif holiday_or_no == 'Y' and (season_type == 'Autumn' or season_type == 'Winter'):
    hriz_price = 3.75
    roses_price = 4.50
    tulip_price = 4.15
    hriz_price += hriz_price * 0.15
    roses_price += roses_price * 0.15
    tulip_price += tulip_price * 0.15
    total_hriz_price = hriz_count * hriz_price
    total_roses_price = roses_count * roses_price
    total_tulip_price = tulip_count * tulip_price
    bucket_price = total_hriz_price + total_roses_price + total_tulip_price
    if season_type == 'Winter' and roses_count >= 10:
        bucket_price *= 0.90


if bucket > 20:
    bucket_price *= 0.80

print(f'{arrange+bucket_price:.2f}')

