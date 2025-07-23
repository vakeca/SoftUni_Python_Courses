key = int(input())
number_of_letters = int(input())
word = ''

for i in range(number_of_letters):
    letter = input()
    ord_of_letter = ord(letter) + key
    word += chr(ord_of_letter)
print(word)
