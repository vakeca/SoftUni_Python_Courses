budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_price_1l = flour_price * 1.25
loaf_price = flour_price + eggs_price + (milk_price_1l / 4)
loaf_count = 0
eggs_count = 0
while loaf_price < budget:
    budget -= loaf_price
    loaf_count += 1
    eggs_count += 3
    if loaf_count % 3 == 0:
        lost_eggs = loaf_count - 2
        eggs_count -= lost_eggs
print(f'You made {loaf_count} loaves of Easter bread! Now you have {eggs_count} eggs and {budget:.2f}BGN left.')