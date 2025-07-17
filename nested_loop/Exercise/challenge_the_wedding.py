men = int(input())
women = int(input())
table_count = int(input())

table_taken = 0
is_all_table_taken = False

for i in range(1, men + 1):
    for j in range(1, women + 1):
        table_taken += 1
        print(f'({i} <-> {j})', end= ' ')
        if table_count <= table_taken:
            is_all_table_taken = True
            break
    if is_all_table_taken:
        break