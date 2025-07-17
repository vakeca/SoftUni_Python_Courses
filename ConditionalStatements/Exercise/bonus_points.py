number = int(input())

bonus_points = 0

if number <= 100:
    bonus_points += 5
elif number > 1000:
    bonus_points += number * 10/100
else:
    bonus_points += number * 20/100

if number % 2 == 0:
    bonus_points += 1
elif number % 5 == 0:
    bonus_points += 2

print(bonus_points)
print(number + bonus_points)