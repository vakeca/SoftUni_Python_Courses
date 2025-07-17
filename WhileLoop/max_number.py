

max_number = int(input())

while True:
    new_number = input()
    if new_number == 'Stop':
        break
    new_number = int(new_number)
    if new_number > max_number:
        max_number = new_number
print(max_number)
