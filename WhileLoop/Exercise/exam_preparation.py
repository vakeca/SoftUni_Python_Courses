bad_grades = int(input())

problems_count = 0
average_grade = 0
bad_grades_count = 0
last_problem = ''

while True:
    problem_name = input()
    if problem_name == 'Enough':
        print(f'Average score: {average_grade / problems_count:.2f}')
        print(f'Number of problems: {problems_count}')
        print(f'Last problem: {last_problem}')
        break
    grade = int(input())
    last_problem = problem_name
    problems_count += 1
    average_grade += grade
    if grade <= 4:
        bad_grades_count += 1
        if bad_grades_count >= bad_grades:
            print(f'You need a break, {bad_grades_count} poor grades.')
            break