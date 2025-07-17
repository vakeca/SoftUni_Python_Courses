first_num = int(input())
second_num = int(input())

for i in range(first_num, second_num + 1):
    current_sum_str = str(i)
    odd_sum = 0
    even_sum = 0
    for symbol_count in range(0, len(current_sum_str)):
        digit = int(current_sum_str[symbol_count])
        if symbol_count % 2 != 0:
            odd_sum += digit
        else:
            even_sum += digit
    if odd_sum == even_sum:
        print(current_sum_str, end= ' ')
