while True:
    command = input()
    if command == 'End':
        break
    if command == 'SoftUni':
        continue
    string = ''
    for i in command:
        string += i * 2
    print(string)