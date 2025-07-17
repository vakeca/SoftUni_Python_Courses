n = int(input())
p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0

for i in range(n):
    user_input = int(input())
    if user_input < 200:
        p1_count += 1
    elif 200 <= user_input <= 399:
        p2_count += 1
    elif 400 <= user_input <= 599:
        p3_count += 1
    elif 600 <= user_input <= 799:
        p4_count += 1
    else:
        p5_count += 1

p1_percentage = p1_count * 100 / n
p2_percentage = p2_count * 100 / n
p3_percentage = p3_count * 100 / n
p4_percentage = p4_count * 100 / n
p5_percentage = p5_count * 100 / n

print(f'{p1_percentage:.2f}%')
print(f'{p2_percentage:.2f}%')
print(f'{p3_percentage:.2f}%')
print(f'{p4_percentage:.2f}%')
print(f'{p5_percentage:.2f}%')