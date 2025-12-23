good = "ABCEHKMOPTX"

n = int(input())
for _ in range(n):
    s = input()
    ok = (
        len(s) == 6 and
        s[0] in good and
        s[1:4].isdigit() and
        s[4] in good and
        s[5] in good
    )
    print("Yes" if ok else "No")
