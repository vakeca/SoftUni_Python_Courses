snowball_count = int(input())
value = 0
max_weight = 0
best_time = 0
best_quality = 0

for snowball in range(snowball_count):
    weight = int(input())
    time = int(input())
    quality = int(input())
    current_value = (weight / time) ** quality
    if current_value > value:
        value = current_value
        max_weight = weight
        best_time = time
        best_quality = quality
print(f'{max_weight} : {best_time} = {int(value)} ({best_quality})')