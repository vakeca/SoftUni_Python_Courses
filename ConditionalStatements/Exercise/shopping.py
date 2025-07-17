budget = float(input())
count_gpu = int(input())
count_cpu = int(input())
count_ram = int(input())

gpu_price = 250 * count_gpu
cpu_price = count_cpu * (gpu_price * 35/100)
ram_price = count_ram * (gpu_price * 10/100)

total_price = gpu_price + cpu_price + ram_price

if count_gpu > count_cpu:
    total_price *= 85/100

money_left = abs(budget - total_price)

if budget >= total_price:
    print(f'You have {money_left:.2f} leva left!')
else:
    print(f'Not enough money! You need {money_left:.2f} leva more!')