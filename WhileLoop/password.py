username = input()
pwd = input()

while True:
    user_input = input()
    if user_input == pwd:
        break
print(f'Welcome {username}!')