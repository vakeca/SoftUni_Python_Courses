floor = int(input())
rooms = int(input())

for i in range(floor, 0, -1):
    for j in range(0, rooms):
        if i == floor:
            print(f'L{i}{j}', end=' ')
        elif i % 2 == 0:
            print(f'O{i}{j}', end=' ')
        else:
            print(f'A{i}{j}', end=' ')

    print()