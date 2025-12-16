a, b, c = map(int, input().split())

# Находим максимум и минимум
maximum = max(a, b, c)
minimum = min(a, b, c)

print(maximum - minimum)