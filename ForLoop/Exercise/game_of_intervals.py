moves = int(input())

total_points = 0
points_in_9_range = 0
points_in_19_range = 0
points_in_29_range = 0
points_in_39_range = 0
points_in_50_range = 0
invalid_points = 0
total_number_of_points = 0

for i in range(1, moves + 1):
    number = int(input())
    total_number_of_points += 1
    number_per_turn = 0
    if 0 <= number <= 9:
        points_in_9_range += 1
        number *= 0.2
        number_per_turn += number
        total_points += number_per_turn
    elif 10 <= number <= 19:
        points_in_19_range += 1
        number *= 0.3
        number_per_turn += number
        total_points += number_per_turn
    elif 20 <= number <= 29:
        points_in_29_range += 1
        number *= 0.4
        number_per_turn += number
        total_points += number_per_turn
    elif 30 <= number <= 39:
        points_in_39_range += 1
        number_per_turn += 50
        total_points += number_per_turn
    elif 40 <= number <= 50:
        points_in_50_range += 1
        number_per_turn += 100
        total_points += number_per_turn
    else:
        invalid_points += 1
        total_points /= 2
        total_points += number_per_turn

print(f'{total_points:.2f}')
print(f'From 0 to 9: {points_in_9_range / total_number_of_points * 100:.2f}%')
print(f'From 10 to 19: {points_in_19_range / total_number_of_points * 100:.2f}%')
print(f'From 20 to 29: {points_in_29_range / total_number_of_points * 100:.2f}%')
print(f'From 30 to 39: {points_in_39_range / total_number_of_points * 100:.2f}%')
print(f'From 40 to 50: {points_in_50_range / total_number_of_points * 100:.2f}%')
print(f'Invalid numbers: {invalid_points / total_number_of_points * 100:.2f}%')



