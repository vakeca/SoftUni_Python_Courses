n = int(input())

even_sum = 0
odd_sum = 0

for i in range(n):
    user_input = int(input())
    if i % 2 == 0:
        even_sum += user_input
    else:
        odd_sum += user_input

if odd_sum == even_sum:
    print(f'Yes')
    print(f'Sum = {even_sum}')
else:
    diff = abs(odd_sum - even_sum)
    print('No')
    print(f'Diff = {diff}')