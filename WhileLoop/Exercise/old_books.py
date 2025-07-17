needed_book = input()

number_of_books = 0

while True:
    current_book = input()
    if current_book == needed_book:
        print(f'You checked {number_of_books} books and found it.')
        break

    elif current_book == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {number_of_books} books.')
        break
    number_of_books += 1