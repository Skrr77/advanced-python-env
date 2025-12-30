import math


def hypotenuse(a, b):
    return math.sqrt(a * a + b * b)

h1 = hypotenuse(3, 4)
h2 = hypotenuse(6, 8)

print("Hypotenuse of first triangle:", h1)
print("Hypotenuse of second triangle:", h2)

if h1 > h2:
    print("First hypotenuse is greater")
else:
    print("Second hypotenuse is greater")




text = input("Enter a string: ")
words = text.split()
sorted_words = []

for word in words:
    sorted_words.append("".join(sorted(word)))

print("Result:", " ".join(sorted_words))
