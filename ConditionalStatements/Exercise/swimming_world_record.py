from math import floor

record_time = float(input())
distance = float(input())
time_per_meter = float(input())

distance_needed = distance * time_per_meter
added_time = floor(distance / 15)
total_added_time = added_time * 12.5
total_time = distance_needed + total_added_time

left_time = abs(total_time - record_time)

if total_time < record_time:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {left_time:.2f} seconds slower.')

