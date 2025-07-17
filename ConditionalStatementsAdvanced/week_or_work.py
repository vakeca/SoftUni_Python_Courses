day = input()
result = ''

if day == 'Saturday' or day == 'Sunday':
    result = "Weekend"
elif day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    result = 'Working day'
else:
    result = 'Error'
print(result)

