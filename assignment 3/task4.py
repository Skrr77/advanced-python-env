# Euclid algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 1. Divide fractions
A, B = 1, 2
C, D = 3, 4

numerator = A * D
denominator = B * C
g = gcd(numerator, denominator)

print("Result:", numerator // g, "/", denominator // g)

# 2. Points inside a circle
def is_inside_circle(x, y, a, b, r):
    return (x - a)**2 + (y - b)**2 <= r**2

a, b, r = 0, 0, 5
points = [(1, 1), (6, 0), (2, 2)]

count = 0
for x, y in points:
    if is_inside_circle(x, y, a, b, r):
        count += 1

print("Number of points inside the circle:", count)
