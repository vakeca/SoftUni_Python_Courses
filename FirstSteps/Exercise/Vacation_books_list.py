# 1. Брой страници в текущата книга – цяло число в интервала [1…1000]
# 2. Страници, които прочита за 1 час – цяло число в интервала [1…1000]
# 3. Броят на дните, за които трябва да прочете книгата – цяло число в интервала [1…1000]

pages_count = int(input())
pph = int(input())
days_count = int(input())
hours_needed = int(pages_count // pph) // days_count
print(hours_needed)