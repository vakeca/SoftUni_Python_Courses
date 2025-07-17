projection_type = input()
row = int(input())
column = int(input())
result = 0

seats_taken = row * column

if projection_type == 'Premiere':
    result = seats_taken * 12
elif projection_type == 'Normal':
    result = seats_taken * 7.5
else:
    result = seats_taken * 5

print(f'{result:.2f}')