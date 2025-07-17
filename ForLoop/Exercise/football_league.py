total_seats = int(input())
total_fans = int(input())

sector_a_total = 0
sector_b_total = 0
sector_v_total = 0
sector_g_total = 0


for i in range(1, total_fans + 1):
    sector = input()
    if sector == 'A':
        sector_a_total += 1
    elif sector == 'B':
        sector_b_total += 1
    elif sector == 'V':
        sector_v_total += 1
    elif sector == 'G':
        sector_g_total += 1

print(f'{sector_a_total / total_fans * 100:.2f}%')
print(f'{sector_b_total / total_fans * 100:.2f}%')
print(f'{sector_v_total / total_fans * 100:.2f}%')
print(f'{sector_g_total / total_fans * 100:.2f}%')
print(f'{total_fans / total_seats * 100:.2f}%')