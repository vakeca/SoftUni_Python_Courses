budget = float(input())
ticket_type = input()
man_count = int(input())

vip = 499.99
normal = 249.99
transport = 0

if 1 <= man_count <= 4:
    transport = budget * 0.75
elif 5 <= man_count <= 9:
    transport = budget * 0.60
elif 10 <= man_count <= 24:
    transport = budget * 0.50
elif 25 <= man_count <= 49:
    transport = budget * 0.40
else:
    transport = budget * 0.25

money_left = abs(budget - transport)

total_vip = 0
total_normal = 0
money_after_vip = 0
money_after_normal = 0

if ticket_type == "VIP":
    total_vip = vip * man_count
    money_after_vip = abs(money_left - total_vip)
else:
    total_normal = normal * man_count
    money_after_normal = abs(money_left - total_normal)


if ticket_type == 'VIP' and money_left > total_vip:
    print(f'Yes! You have {money_after_vip:.2f} leva left.')
elif ticket_type == 'Normal' and money_left > total_normal:
    print(f'Yes! You have {money_after_normal:.2f} leva left.')
elif ticket_type == 'VIP' and money_left < total_vip:
    print(f'Not enough money! You need {money_after_vip:.2f} leva.')
else:
    print(f'Not enough money! You need {money_after_normal:.2f} leva.')
