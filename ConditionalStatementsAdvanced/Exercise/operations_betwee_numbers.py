num1 = int(input())
num2 = int(input())
operator = input()

result = 0
numer_type = ''

if operator == '+' or operator == '-' or operator == '*':
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2

    if result % 2 == 0:
        numer_type = 'even'
    else:
        numer_type = 'odd'

    print(f'{num1} {operator} {num2} = {result} - {numer_type}')

elif operator == '/' and num2 != 0:
        if operator == '/':
            result = num1 / num2
            print(f'{num1} {operator} {num2} = {result:.2f}')
elif operator == '%' and num2 != 0:
        if operator == '%':
            result = num1 % num2
            print(f'{num1} {operator} {num2} = {result}')

if num2 == 0:
    print(f'Cannot divide {num1} by zero')
