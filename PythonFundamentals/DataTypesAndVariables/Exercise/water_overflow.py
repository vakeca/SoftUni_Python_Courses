pouring_count = int(input())
tank_capacity = 255
liters_poured = 0

for liters in range(pouring_count):
    current_liters = int(input())
    if current_liters + liters_poured > tank_capacity:
        print('Insufficient capacity!')
        continue
    liters_poured += current_liters
print(liters_poured)