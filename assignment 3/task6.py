import math

# Euclid algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 1. GCD and LCM
A, B = 12, 18
g = gcd(A, B)
lcm = (A * B) // g

print("GCD:", g)
print("LCM:", lcm)

# 2. Area of convex quadrilateral
a, b, c, d, diag = 4, 5, 6, 7, 8

s1 = (a + b + diag) / 2
s2 = (c + d + diag) / 2

area1 = math.sqrt(s1 * (s1 - a) * (s1 - b) * (s1 - diag))
area2 = math.sqrt(s2 * (s2 - c) * (s2 - d) * (s2 - diag))

print("Quadrilateral area:", area1 + area2)
