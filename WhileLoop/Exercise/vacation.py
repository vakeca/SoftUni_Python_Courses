vacation_price = float(input())
initial_money = float(input())

spend_streak = 0
days_count = 0

while True:
    action = input()
    money = float(input())
    days_count += 1
    if action == 'spend':
        spend_streak += 1
        initial_money -= money
        if initial_money < 0:
            initial_money = 0
    elif action == 'save':
        spend_streak = 0
        initial_money += money

    if initial_money >= vacation_price:
        print(f'You saved the money for {days_count} days.')
        break
    if spend_streak >= 5:
        print('You can\'t save the money.')
        print(days_count)
        break