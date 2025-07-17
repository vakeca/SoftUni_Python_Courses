goal = 10000
all_steps = 0
diff = abs(goal - all_steps)

is_goal_reached = False

while all_steps <= goal:
    steps = input()
    if steps == 'Going home':
        steps = int(input())
        all_steps += steps
        diff = abs(goal - all_steps)
        if all_steps >= goal:
            is_goal_reached = True
            break
        else:
            print(f'{diff} more steps to reach goal.')
            break
    else:
        steps = int(steps)
        all_steps += steps
        diff = abs(goal - all_steps)

    if all_steps >= goal:
        print('Goal reached! Good job!')
        print(f'{diff} steps over the goal!')

if is_goal_reached:
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')