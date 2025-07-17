actor_name = input()
academy_points = float(input())
n = int(input())

has_required_points = False
threshold = 1250.5

for i in range(n):
    judge = input()
    points = float(input())
    academy_points = academy_points + ((len(judge) * points) / 2 )

    if academy_points > threshold:
        has_required_points = True
        break
    else:
        has_required_points = False

if has_required_points:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!')
else:
    print(f'Sorry, {actor_name} you need {threshold - academy_points:.1f} more!')




