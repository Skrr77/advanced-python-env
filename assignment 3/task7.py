# 1. Area of quadrilateral with right angle
def right_triangle_area(a, b):
    return a * b / 2

def rectangle_area(a, b):
    return a * b

X, Y, Z, T = 3, 4, 5, 6

area = right_triangle_area(X, Y) + rectangle_area(Z, T)
print("Area:", area)

# 2. Convert to 10-digit octal
n = int(input("Enter number: "))
print("Octal:", format(n, "010o"))
