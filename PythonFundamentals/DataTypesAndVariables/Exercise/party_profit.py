from math import floor

party_size = int(input())
days = int(input())
total_coins = 0

for day in range(1, days + 1):
    total_coins += 50
    if day % 10 == 0:
        party_size -= 2
    if day % 15 == 0:
        party_size += 5
    total_coins -= 2 * party_size
    if day % 3 == 0:
        total_coins -= 3 * party_size
    if day % 5 == 0:
        total_coins += 20 * party_size
        if day % 3 == 0:
            total_coins -= 2 * party_size
coins_each = floor(total_coins / party_size)
print(f'{party_size} companions received {coins_each} coins each.')