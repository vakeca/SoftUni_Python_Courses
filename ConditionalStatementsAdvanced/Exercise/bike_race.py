junior_count = int(input())
seniors_count = int(input())
race_type = input()

total_participants = junior_count + seniors_count
money_left = 0

if race_type == 'trail':
    junior_price = junior_count * 5.5
    seniors_price = seniors_count * 7
    total_price = junior_price + seniors_price
    expenses = total_price * 0.05
    money_left = total_price - expenses
elif race_type == 'cross-country':
        if total_participants >= 50:
            junior_price = junior_count * 8
            seniors_price = seniors_count * 9.50
            total_price = junior_price + seniors_price
            total_price *= 0.75
            expenses = total_price * 0.05
            money_left = total_price - expenses
        else:
                junior_price = junior_count * 8
                seniors_price = seniors_count * 9.5
                total_price = junior_price + seniors_price
                expenses = total_price * 0.05
                money_left = total_price - expenses

elif race_type == 'downhill':
    junior_price = junior_count * 12.25
    seniors_price = seniors_count * 13.75
    total_price = junior_price + seniors_price
    expenses = total_price * 0.05
    money_left = total_price - expenses
else:
    junior_price = junior_count * 20
    seniors_price = seniors_count * 21.5
    total_price = junior_price + seniors_price
    expenses = total_price * 0.05
    money_left = total_price - expenses

print(f'{money_left:.2f}')