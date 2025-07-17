grp_count = int(input())

grp_5 = 0
grp_12 = 0
grp_25 = 0
grp_40 = 0
grp_41 = 0

total_ppl = 0

for i in range(grp_count):
    people_count = int(input())
    total_ppl = total_ppl + people_count
    if people_count <= 5:
        grp_5 += people_count
    elif 6 <= people_count <= 12:
        grp_12 += people_count
    elif 13 <= people_count <= 25:
        grp_25 += people_count
    elif 26 <= people_count <= 40:
        grp_40 += people_count
    else:
        grp_41 += people_count

print(f'{(grp_5 / total_ppl) * 100:.2f}%')
print(f'{(grp_12 / total_ppl) * 100:.2f}%')
print(f'{(grp_25 / total_ppl) * 100:.2f}%')
print(f'{(grp_40 / total_ppl) * 100:.2f}%')
print(f'{(grp_41 / total_ppl) * 100:.2f}%')