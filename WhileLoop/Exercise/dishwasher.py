bottles = int(input())
detergent_ml = bottles * 750

clean_dishes = 0
clean_pots = 0
counter = 0

line_input = input()
while line_input != 'End':
    counter += 1
    dishes = int(line_input)
    if counter % 3 == 0:
        clean_pots += dishes
        pots_ml = 15 * dishes
        detergent_ml -= pots_ml
    else:
        clean_dishes += dishes
        dishes_ml = 5 * dishes
        detergent_ml -= dishes_ml

    if detergent_ml < 0:
        break

    line_input = input()


if detergent_ml < 0:
    print(f'Not enough detergent, {abs(detergent_ml)} ml. more necessary!')
else:
    print('Detergent was enough!')
    print(f'{clean_dishes} dishes and {clean_pots} pots were washed.')
    print(f'Leftover detergent {detergent_ml} ml.')