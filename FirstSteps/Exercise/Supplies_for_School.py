pen_count = int(input())
marker_count = int(input())
detergent_liters = int(input())
discount = int(input())

price_pen = 5.80
price_marker = 7.20
price_detergent = 1.20

total_price = (pen_count * price_pen) + (marker_count * price_marker) + (detergent_liters * price_detergent)
total_price_after_discount = total_price - (total_price * discount / 100)
print(total_price_after_discount)