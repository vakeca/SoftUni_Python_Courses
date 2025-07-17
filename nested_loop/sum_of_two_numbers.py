first_number = int(input())
second_number = int(input())
magic_number = int(input())

combinations = 0

is_found = False

for number_one in range(first_number, second_number + 1):
    for number_two in range(first_number, second_number + 1):
        combinations += 1
        if number_one + number_two == magic_number:
            is_found = True
            print(f'Combination N:{combinations} ({number_one} + {number_two} = {magic_number})')
            break
    if is_found:
        break

else:
    print(f'{combinations} combinations - neither equals {magic_number}')