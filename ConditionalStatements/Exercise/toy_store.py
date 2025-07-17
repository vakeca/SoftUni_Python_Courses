price_trip = float(input())
count_puzzels = int(input())
count_dolls = int(input())
count_bears = int(input())
count_minions = int(input())
count_trucks = int(input())

total_sum = (count_puzzels * 2.60 + count_dolls * 3 + count_bears * 4.10 + count_minions * 8.20 + count_trucks * 2)
total_sum_toys = count_puzzels + count_dolls + count_bears + count_minions + count_trucks

if total_sum_toys >= 50:
    total_sum = total_sum - (total_sum * 25 / 100)

total_sum *= 90/100

if total_sum >= price_trip:
    print(f'Yes! {total_sum - price_trip:.2f} lv left.')
else:
    print(f"Not enough money! {price_trip - total_sum:.2f} lv needed.")