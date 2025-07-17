hour = int(input())
work_day = input()

if hour >= 10 and hour <= 18 and work_day != 'Sunday':
    print('open')
else:
    print('closed')