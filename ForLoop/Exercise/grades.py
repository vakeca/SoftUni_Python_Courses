number_of_students = int(input())

average_score = 0
total_top_students = 0
total_4_students = 0
total_3_students = 0
total_fail_students = 0

for i in range(1, number_of_students + 1):
    grade = float(input())
    if grade >= 5.00:
        total_top_students += 1
        average_score += grade / number_of_students
    elif 4.00 <= grade <= 4.99:
        total_4_students += 1
        average_score += grade / number_of_students
    elif 3.00 <= grade <= 3.99:
        total_3_students += 1
        average_score += grade / number_of_students
    else:
        total_fail_students += 1
        average_score += grade / number_of_students

print(f'Top students: {total_top_students / number_of_students * 100:.2f}%')
print(f'Between 4.00 and 4.99: {total_4_students / number_of_students * 100:.2f}%')
print(f'Between 3.00 and 3.99: {total_3_students / number_of_students * 100:.2f}%')
print(f'Fail: {total_fail_students / number_of_students * 100:.2f}%')
print(f'Average: {average_score:.2f}')