lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmet_count = 0
broken_sword_count = 0
broken_shield_count = 0
broken_armor_count = 0

for lose in range(1, lost_fights_count + 1):
    if lose % 2 == 0:
        broken_helmet_count += 1
    if lose % 3 == 0:
        broken_sword_count += 1
        if lose % 2 == 0:
            broken_shield_count += 1
    if lose % 12 == 0:
        broken_armor_count += 1

total_helmet_price = broken_helmet_count * helmet_price
total_sword_price = broken_sword_count * sword_price
total_shield_price = broken_shield_count * shield_price
total_armor_price = broken_armor_count * armor_price
total_price = total_helmet_price + total_sword_price + total_shield_price + total_armor_price
print(f'Gladiator expenses: {total_price:.2f} aureus')