budget = int(input())
total_price = 0


while True:
    line_input = input()
    if line_input == 'End':
        print(f'You bought everything needed.')
        break
    price = int(line_input)
    if total_price + price > budget:
        print('You went in overdraft!')
        break
    total_price += price