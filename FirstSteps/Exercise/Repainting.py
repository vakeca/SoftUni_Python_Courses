fixed_nylon_price = 1.50
fixed_paint_price = 14.50
fixed_thinner = 5.00

nylon_count = int(input())
paint_count = int(input())
thinner_count = int(input())
work_hours = int(input())

nylon_price = (nylon_count + 2) * fixed_nylon_price
paint_price = (paint_count + (paint_count * 10/100)) * fixed_paint_price
thinner_price = thinner_count * fixed_thinner
bags = 0.40

total_material_price = nylon_price + paint_price + thinner_price + bags
worker_payment = (total_material_price * 30/100) * work_hours
total_price = total_material_price + worker_payment
print(total_price)