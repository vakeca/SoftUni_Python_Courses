decoration_qty = int(input())
days_left = int(input())

ornament_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

total_price = 0
total_spirit = 0

for days in range(1, days_left + 1):
    if days % 11 == 0:
        decoration_qty += 2
    if days % 2 == 0:
        total_price += ornament_price * decoration_qty
        total_spirit += 5
    if days % 3 == 0:
        total_price += (tree_skirt_price + tree_garland_price) * decoration_qty
        total_spirit += 13
    if days % 5 == 0:
        total_price += tree_lights_price * decoration_qty
        total_spirit += 17
        if days % 3 == 0:
            total_spirit += 30
    if days % 10 == 0:
        total_spirit -= 20
        total_price += tree_skirt_price + tree_garland_price + tree_lights_price
    if days == days_left and days_left % 10 == 0:
        total_spirit -= 30
print(f'Total cost: {total_price}')
print(f'Total spirit: {total_spirit}')