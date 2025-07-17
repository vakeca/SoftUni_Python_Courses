key_letter_c = 'c'
key_letter_o = 'o'
key_letter_n = 'n'

word = ''
secret_word = ''
secret_word_counter = 0
c_counter = 0
o_counter = 0
n_counter = 0

while True:
    if secret_word_counter == 3:
        print(f'{word} ', end='' )
        secret_word_counter = 0
        c_counter = 0
        o_counter = 0
        n_counter = 0
        word = ''

    line_input = input()
    if line_input == 'End':
        break

    if 'a' <= line_input <= 'z' or 'A' <= line_input <= 'Z':
        if line_input == key_letter_c:
            c_counter += 1
            if c_counter == 1:
                secret_word_counter += 1
                secret_word += line_input
                continue
            else:
                word += line_input
                continue
        elif line_input == key_letter_o:
            o_counter += 1
            if o_counter == 1:
                secret_word_counter += 1
                secret_word += line_input
                continue
            else:
                word += line_input
                continue
        elif line_input == key_letter_n:
            n_counter += 1
            if n_counter == 1:
                secret_word_counter += 1
                secret_word += line_input
                continue
            else:
                word += line_input
                continue

        word += line_input