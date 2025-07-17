while True:
    destination = input()
    if destination == 'End':
        break
    price = float(input())
    current_money = 0
    while current_money < price:
        current_money += float(input())

    print(f'Going to {destination}!')