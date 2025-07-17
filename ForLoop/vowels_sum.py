user_input = input()

total = 0

for i in range(0, len(user_input)):
    char = user_input[i]
    if char == 'a':
        total += 1
    elif char == 'e':
        total += 2
    elif char == 'i':
        total += 3
    elif char == 'o':
        total += 4
    elif char == 'u':
        total += 5

print(total)