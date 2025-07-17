season_type = input()
grp_type = input()
student_count = int(input())
stay_count = int(input())

boys_winter = 9.6
girls_winter = 9.6
mixed_winter = 10

boys_spring = 7.2
girls_spring = 7.2
mixed_spring = 9.5

boys_summer = 15
girls_summer = 15
mixed_summer = 20

sport_type = ''
price = 0

if grp_type == 'girls':
    if season_type == 'Winter':
        sport_type = 'Gymnastics'
        price = girls_winter * stay_count * student_count
    elif season_type == 'Spring':
        sport_type = 'Athletics'
        price = girls_spring * stay_count * student_count
    elif season_type == 'Summer':
        sport_type = 'Volleyball'
        price = girls_summer * stay_count * student_count
elif grp_type == 'boys':
    if season_type == 'Winter':
        sport_type = 'Judo'
        price = boys_winter * stay_count * student_count
    elif season_type == 'Spring':
        sport_type = 'Tennis'
        price = boys_spring * stay_count * student_count
    elif season_type == 'Summer':
        sport_type = 'Football'
        price = boys_summer * stay_count * student_count
else:
    if season_type == 'Winter':
        sport_type = 'Ski'
        price = mixed_winter * stay_count * student_count
    elif season_type == 'Spring':
        sport_type = 'Cycling'
        price = mixed_spring * stay_count * student_count
    else:
        sport_type = 'Swimming'
        price = mixed_summer * stay_count * student_count

if student_count < 10:
    price = price
elif 10 <= student_count < 20:
    price *= 0.95
elif 20 <= student_count < 50:
    price *= 0.85
else:
    price *= 0.50

print(f'{sport_type} {price:.2f} lv.')
