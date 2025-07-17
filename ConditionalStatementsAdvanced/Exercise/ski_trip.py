stay_count = int(input()) -1
room_type = input()
review = input()

room_for_one_person = 18
apartment = 25
president_apartment = 35

if stay_count < 10:
    apartment *= 0.70
    president_apartment *= 0.90
elif 10 <= stay_count <= 15:
    apartment *= 0.65
    president_apartment *= 0.85
else:
    apartment *= 0.50
    president_apartment *= 0.80

total_room = stay_count * room_for_one_person
total_apartment = stay_count * apartment
total_president = stay_count * president_apartment

if review == 'positive':
    total_room = total_room + total_room * 0.25
    total_apartment = total_apartment + total_apartment * 0.25
    total_president = total_president + total_president * 0.25
else:
    total_room = total_room - total_room * 0.1
    total_apartment = total_apartment - total_apartment * 0.1
    total_president = total_president - total_president * 0.1

if room_type == 'room for one person':
    print(f'{total_room:.2f}')
elif room_type == 'apartment':
    print(f'{total_apartment:.2f}')
else:
    print(f'{total_president:.2f}')
