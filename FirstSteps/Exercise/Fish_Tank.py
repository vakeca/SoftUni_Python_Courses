a = int(input())
b = int(input())
c = int(input())
percent = float(input())

area = a * b * c
liters_area = area / 1000
taken_area = percent / 100

liters_needed = liters_area * (1 - taken_area)
print(liters_needed)