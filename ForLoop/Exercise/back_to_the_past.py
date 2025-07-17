legacy = float(input())
year_to_live = int(input())

age = 18

for i in range(1800, year_to_live + 1):
    if i != 1800:
        age += 1

    if i % 2 == 0:
        legacy -= 12000
    else:
        age_cost = 50 * age
        cost = 12000 + age_cost
        legacy -= cost


if legacy >= 0:
    print(f'Yes! He will live a carefree life and will have {legacy:.2f} dollars left.')
else:
    print(f'He will need {abs(legacy):.2f} dollars to survive.')