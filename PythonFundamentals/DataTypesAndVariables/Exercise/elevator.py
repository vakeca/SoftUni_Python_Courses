number_of_people = int(input())
elevator_capacity = int(input())

full_courses = number_of_people // elevator_capacity
courses = full_courses
if number_of_people % elevator_capacity != 0:
    courses += 1
print(courses)