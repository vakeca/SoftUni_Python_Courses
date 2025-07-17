from math import floor

turnir_count = int(input())
initial_points = int(input())

W = 2000
F = 1200
SF = 720

average_points = 0
win_count = 0

for i in range(turnir_count):
    position = input()
    if position == 'W':
        win_count += 1
        initial_points += W
        average_points += W
    elif position == 'F':
        initial_points += F
        average_points += F
    else:
        initial_points += SF
        average_points += SF

average_points /= turnir_count

print(f'Final points: {initial_points}')
print(f'Average points: {floor(average_points)}')
print(f'{win_count / turnir_count * 100:.2f}%')
