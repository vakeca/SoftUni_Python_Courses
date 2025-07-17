student_name = input()

class_number = 1
average_grade = 0
fail = 0

while True:
    grade = float(input())
    if grade < 4:
        fail += 1
        if fail >= 2:
            print(f'{student_name} has been excluded at {class_number} grade')
            break
        continue
    class_number += 1
    average_grade += grade
    if class_number > 12:
        print(f'{student_name} graduated. Average grade: {average_grade / 12:.2f}')
        break