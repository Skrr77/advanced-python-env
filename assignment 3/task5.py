# Euclid algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 1. Subtract fractions
A, B = 5, 6
C, D = 1, 3

numerator = A * D - C * B
denominator = B * D
g = gcd(abs(numerator), denominator)

print("Result:", numerator // g, "/", denominator // g)

# 2. Divisors of a number
n = int(input("Enter number: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
