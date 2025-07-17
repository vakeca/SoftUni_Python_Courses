n = int(input())
combination_count = 0

for x1 in range(n + 1):
    for x2 in range(n + 1):
        for x3 in range(n + 1):
            sum = x1 + x2 + x3
            if sum == n:
                combination_count += 1
print(combination_count)