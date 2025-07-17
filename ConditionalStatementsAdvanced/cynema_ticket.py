day = input()
result = 0

if day == 'Wednesday' or day == 'Thursday':
    result = 14
elif day == 'Saturday' or day == 'Sunday':
    result = 16
elif day == 'Monday' or day == 'Tuesday' or day == 'Friday':
    result = 12

print(result)