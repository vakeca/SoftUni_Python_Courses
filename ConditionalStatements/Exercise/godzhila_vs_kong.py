film_budget = float(input())
statist_count = int(input())
clothes_price = float(input())

if statist_count >= 150:
    clothes_price *= 90 / 100

total_sum_clothes = clothes_price * statist_count
decor_price = film_budget * 10/100
total_price = decor_price + total_sum_clothes

left_money = abs(film_budget - total_price)

if total_price > film_budget:
    print('Not enough money!')
    print(f'Wingard needs {left_money:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {left_money:.2f} leva left.')