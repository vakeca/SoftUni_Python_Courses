number_of_lines = int(input())
opening_bracket = 0
closing_bracket = 0
is_balanced = False
is_unbalanced_forever = True

for i in range(number_of_lines):
    symbol = input()
    if symbol == ')' and opening_bracket == 0:
        is_balanced = False
        is_unbalanced_forever = False
        continue
    if symbol == '(':
        opening_bracket += 1
        if opening_bracket > 1 and closing_bracket == 0:
            is_unbalanced_forever = False
    if symbol == ')':
        closing_bracket += 1
        if opening_bracket == closing_bracket:
            is_balanced = True

if is_balanced and is_unbalanced_forever:
    print('BALANCED')
else:
    print('UNBALANCED')