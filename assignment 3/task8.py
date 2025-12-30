# 1. Numbers divisible by all their digits
n = int(input("Enter n: "))

for i in range(1, n + 1):
    digits = [int(d) for d in str(i) if d != '0']
    if digits and all(i % d == 0 for d in digits):
        print(i, end=" ")

print()

# 2. Swap first and last elements
def swap_first_last(arr):
    arr[0], arr[-1] = arr[-1], arr[0]

m = int(input("Enter array length: "))
arr = []

for _ in range(m):
    arr.append(int(input()))

print("Original array:", arr)
swap_first_last(arr)
print("Modified array:", arr)
