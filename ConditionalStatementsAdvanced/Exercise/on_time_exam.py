exam_hour = int(input())
exam_minutes = int(input())
arrive_hour = int(input())
arrive_minutes = int(input())

exam_hour_in_min = exam_hour * 60
arrive_hour_in_min = arrive_hour * 60

exam_all_min = exam_hour_in_min + exam_minutes
arrive_all_min = arrive_hour_in_min + arrive_minutes

diff = abs(exam_all_min - arrive_all_min)

if arrive_all_min > exam_all_min:
    print('Late')
    if diff < 60:
        print(f'{diff} minutes after the start')
    else:
        hours = diff // 60
        minutes = diff % 60
        if minutes < 10:
            print(f'{hours}:0{minutes} hours after the start')
        else:
            print(f'{hours}:{minutes} hours after the start')

elif arrive_all_min == exam_all_min or diff <= 30:
    print('On time')
    if diff != 0:
        print(f'{diff} minutes before the start')
elif arrive_all_min < exam_all_min or diff > 30:
    print('Early')
    if diff < 60:
        print(f'{diff} minutes before the start')
    else:
        hours = diff // 60
        minutes = diff % 60
        if minutes < 10:
            print(f'{hours}:0{minutes} hours before the start')
        else:
            print(f'{hours}:{minutes} hours before the start')