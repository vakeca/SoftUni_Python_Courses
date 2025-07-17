goal = 10000
all_steps = 0

diff = abs(all_steps - goal)


while True:
    steps = input()
    if steps == 'Going home':
        steps = int(input())
        all_steps += steps
        if all_steps >= goal:
            print('Goal reached! Good job!')
            print(f'{diff} steps over the goal!')
            break
        break
    steps = int(steps)
    all_steps += steps
    diff = abs(all_steps - goal)
    if all_steps >= goal:
        print('Goal reached! Good job!')
        print(f'{diff} steps over the goal!')
        break

diff = abs(all_steps - goal)

if all_steps < goal:
    print(f'{diff} more steps to reach goal.')
