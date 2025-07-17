width = int(input())
length = int(input())
height = int(input())

volume = width * length * height
is_space_enough = False

input_line = input()

while input_line != 'Done':
    cubic_meters = int(input_line)
    volume -= cubic_meters
    if volume <= 0:
        is_space_enough = True
        break
    input_line = input()

if is_space_enough:
    print(f'No more free space! You need {abs(volume)} Cubic meters more.')
else:
    print(f'{volume} Cubic meters left.')