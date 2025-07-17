age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

number_of_toys = 0
money_for_birthday = 10
saved_money = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        saved_money += (money_for_birthday - 1)
        money_for_birthday += 10
    else:
        number_of_toys += 1

toys_total_price = number_of_toys * toy_price
total_sum = toys_total_price + saved_money
diff = abs(washing_machine_price - total_sum)

if total_sum >= washing_machine_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')