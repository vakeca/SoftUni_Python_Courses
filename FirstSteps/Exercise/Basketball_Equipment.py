yearly_fee = int(input())

shoes = yearly_fee - (yearly_fee * 40/100)
clothes = shoes - (shoes * 20/100)
ball = clothes * 25/100
accessories = ball * 20/100

total_sum = yearly_fee + shoes + clothes + ball + accessories
print(total_sum)