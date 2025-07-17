chicken_menu = 10.35
fish_menu = 12.40
vegan_menu = 8.15

chicken_count = int(input())
fish_count = int(input())
vegan_count = int(input())

chicken_price = chicken_count * chicken_menu
fish_price = fish_count * fish_menu
vegan_price = vegan_count * vegan_menu

total_price_without_desert = chicken_price + fish_price + vegan_price
with_desert = total_price_without_desert * 20/100
total_sum = total_price_without_desert + with_desert + 2.50
print(total_sum)