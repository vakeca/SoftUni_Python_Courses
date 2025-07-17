n = int(input())

first = 0
second = 0
third = 0
forth = 0

for i in range(n * 2):
    number = int(input())
    if n == 3:
        if i == 0:
            first += number
        elif i == 1:
            first += number
        elif i == 2:
            second += number
        elif i == 3:
            second += number
        elif i == 4:
            third += number
        elif i == 5:
            third += number

    elif n == 2:
        if i == 0:
            first += number
        elif i == 1:
            first += number
        elif i == 2:
            second += number
        elif i == 3:
            second += number

    elif n == 1:
        if i == 0:
            first += number
        elif i == 1:
            first += number

    elif n == 4:
        if i == 0:
            first += number
        elif i == 1:
            first += number
        elif i == 2:
            second += number
        elif i == 3:
            second += number
        elif i == 4:
            third += number
        elif i == 5:
            third += number
        elif i == 6:
            forth += number
        elif i == 7:
            forth += number

if n == 1:
    if first == second:
        print(f'Yes, value={first}')
if first == second and third == second:
    print(f'Yes, value={first}')
