import sys

n = int(input())
sum = 0
max_numer = -sys.maxsize

for i in range(n):
    number = int(input())
    sum += number
    if number > max_numer:
        max_numer = number

sum = sum - max_numer

if sum == max_numer:
    print('Yes')
    print(f'Sum = {max_numer}')
else:
    print('No')
    print(f'Diff = {abs(max_numer - sum)}')
