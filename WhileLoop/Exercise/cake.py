width = int(input())
length = int(input())

pieces_count = width * length
is_cake_gone = False

pieces_taken = input()

while pieces_taken != 'STOP':
    pieces_taken = int(pieces_taken)
    pieces_count -= pieces_taken
    if pieces_count <= 0:
        is_cake_gone = True
        break
    pieces_taken = input()

if is_cake_gone:
    print(f'No more cake left! You need {abs(pieces_count)} pieces more.')
else:
    print(f'{pieces_count} pieces are left.')