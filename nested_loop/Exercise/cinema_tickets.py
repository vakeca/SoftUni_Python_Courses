student_seats = 0
standard_seats = 0
kid_seats = 0
is_finish_there = False
while True:
    movie = input()
    if movie == 'Finish':
        break
    free_seats = int(input())
    ticket_type = input()
    total_seats = 0
    while ticket_type != 'End':
        if ticket_type == 'Finish':
            is_finish_there = True
            break
        if ticket_type == 'student':
            total_seats += 1
            student_seats += 1
        elif ticket_type == 'standard':
            total_seats += 1
            standard_seats += 1
        else:
            total_seats += 1
            kid_seats += 1

        if total_seats >= free_seats:
            break
        ticket_type = input()

    if is_finish_there:
        break

    movie_percentage = total_seats / free_seats * 100
    print(f'{movie} - {movie_percentage:.2f}% full.')

all_tickets = student_seats + standard_seats + kid_seats
avg_students = student_seats / all_tickets * 100
avg_standard = standard_seats / all_tickets * 100
avg_kids = kid_seats / all_tickets * 100

print(f'Total tickets: {all_tickets}')
print(f'{avg_students:.2f}% student tickets.')
print(f'{avg_standard:.2f}% standard tickets.')
print(f'{avg_kids:.2f}% kids tickets.')