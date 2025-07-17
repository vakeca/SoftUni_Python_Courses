min_number = int(input())

while True:
    new_number = input()
    if new_number == 'Stop':
        break
    new_number = int(new_number)
    if new_number < min_number:
        min_number = new_number
print(min_number)
