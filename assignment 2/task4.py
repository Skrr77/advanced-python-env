n, m = map(int, input().split())
s = input()

res = []
for i in range(n - m + 1):
    if s[i:i+m] not in res:
        res.append(s[i:i+m])

print(len(res))
