load_count = int(input())

total_microbus_load = 0
total_truck_load = 0
total_train_load = 0

total_microbus_price = 0
total_truck_price = 0
total_train_price = 0


average_price = 0
total_load = 0

for i in range(1, load_count +1):
    microbus_load = 0
    truck_load = 0
    train_load = 0
    load_size = int(input())
    if load_size <= 3:
        microbus_load = load_size
        microbus_price = load_size * 200
        total_microbus_price += microbus_price
    elif 4 <= load_size <= 11:
        truck_load = load_size
        truck_price = load_size * 175
        total_truck_price += truck_price
    else:
        train_load = load_size
        train_price = load_size * 120
        total_train_price += train_price

    total_microbus_load += microbus_load
    total_truck_load += truck_load
    total_train_load += train_load
    total_price = total_microbus_price + total_train_price + total_truck_price
    total_load = total_microbus_load + total_truck_load + total_train_load
    average_price = total_price / total_load

print(f'{average_price:.2f}')
print(f'{total_microbus_load / total_load * 100:.2f}%')
print(f'{total_truck_load / total_load * 100:.2f}%')
print(f'{total_train_load / total_load * 100:.2f}%')