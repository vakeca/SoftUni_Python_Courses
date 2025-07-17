flower_type = input()
qty = int(input())
budget = int(input())
final_price = 0

if flower_type == 'Roses':
    final_price = qty * 5
    if qty > 80:
        final_price = final_price - final_price * 0.10
elif flower_type == 'Dahlias':
    final_price = qty * 3.8
    if qty > 90:
        final_price = final_price - final_price * 0.15
elif flower_type == 'Tulips':
    final_price = qty * 2.8
    if qty > 80:
        final_price = final_price - final_price * 0.15
elif flower_type == 'Narcissus':
    final_price = qty * 3
    if qty < 120:
        final_price = final_price + final_price * 0.15
elif flower_type == 'Gladiolus':
    final_price = qty * 2.5
    if qty < 80:
        final_price = final_price + final_price * 0.2

money_left = abs(final_price - budget)
if final_price <= budget:
    print(f'Hey, you have a great garden with {qty} {flower_type} and {money_left:.2f} leva left.')
else:
    print(f'Not enough money, you need {money_left:.2f} leva more.')