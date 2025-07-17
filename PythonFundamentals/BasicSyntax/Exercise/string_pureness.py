string_number = int(input())

for i in range(string_number):
    string = input()
    is_not_pure = False
    for string_char in string:
        if string_char == ',' or string_char == '.' or string_char == '_':
            is_not_pure = True
            break
    if is_not_pure:
        print(f'{string} is not pure!')
    else:
        print(f'{string} is pure.')