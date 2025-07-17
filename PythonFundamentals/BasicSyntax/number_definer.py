n = float(input())

if n == 0:
    print('zero')
elif 0 < n < 1:
    print('small positive')
elif 0 < n < 1000000:
    print('positive')
elif n > 1000000:
    print('large positive')
elif abs(n) < 1 and abs(n) != 0:
    print('small negative')
elif 0 < abs(n) < 1000000:
    print('negative')
else:
    print('large negative')