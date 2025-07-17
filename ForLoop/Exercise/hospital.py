period = int(input())

doctors = 7
treated_patients = 0
untreated_patients = 0

for i in range(1, period + 1):
    daily_treated = 0
    daily_untreated = 0
    if i % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1
    patients = int(input())

    if doctors >= patients:
        daily_treated = patients
        daily_untreated = 0
    elif doctors < patients:
        daily_untreated = patients - doctors
        daily_treated = patients - daily_untreated

    treated_patients += daily_treated
    untreated_patients += daily_untreated



print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')