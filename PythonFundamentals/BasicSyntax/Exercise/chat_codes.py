number_of_messages = int(input())

for i in range(number_of_messages):
    chat_code = int(input())
    if chat_code == 88:
        print('Hello')
    elif chat_code == 86:
        print('How are you?')
    elif chat_code < 88:
        print('GREAT!')
    else:
        print('Bye.')