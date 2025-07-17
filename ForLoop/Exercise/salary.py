n = int(input())
salary = int(input())

flag = False

for i in range(n):
    opened_tab = input()
    if opened_tab == 'Facebook':
        salary -= 150
    elif opened_tab == 'Instagram':
        salary -= 100
    elif opened_tab == 'Reddit':
        salary -= 50
    if salary <= 0:
        flag = True
        break

if flag:
    print('You have lost your salary.')
else:
    print(f'{salary:.0f}')