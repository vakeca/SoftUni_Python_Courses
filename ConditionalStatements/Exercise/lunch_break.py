from math import ceil

tv_name1 = input()
episode_duration = int(input())
lunch_break_duration = int(input())

lunch_time = lunch_break_duration / 8
relax_time = lunch_break_duration / 4

time_left = lunch_break_duration - lunch_time - relax_time
time_left_after_tv = abs(episode_duration - time_left)

if time_left >= episode_duration:
    print(f'You have enough time to watch {tv_name1} and left with {ceil(time_left_after_tv)} minutes free time.')
else:
    print(f"You don't have enough time to watch {tv_name1}, you need {ceil(time_left_after_tv)} more minutes.")