
needed_money = int(input())

card_counter = 0
cash_counter = 0
counter = 0

average_cash = 0
average_card = 0
money_earned = 0

line_input = input()
while line_input != 'End':
    product_price = int(line_input)
    if counter % 2 == 0:
        if product_price > 100:
            print('Error in transaction!')
        elif 10 <= product_price <= 100:
            cash_counter += 1
            average_cash += product_price
            money_earned += product_price
            print('Product sold!')
    elif counter % 2 == 1:
        if product_price < 10:
            print('Error in transaction!')
        else:
            card_counter += 1
            average_card += product_price
            money_earned += product_price
            print('Product sold!')
    counter += 1

    if money_earned >= needed_money:
        print(f'Average CS: {average_cash / cash_counter:.2f}')
        print(f'Average CC: {average_card / card_counter:.2f}')
        break

    line_input = input()

if line_input == 'End':
    print('Failed to collect required money for charity.')