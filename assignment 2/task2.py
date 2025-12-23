a = input()
b = input()

n = len(b)
b2 = b + b
shifts = []

for i in range(n):
    shifts.append(b2[i:i+n])

ans = 0
for i in range(len(a) - n + 1):
    if a[i:i+n] in shifts:
        ans += 1

print(ans)
