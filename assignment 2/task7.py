items = input().split()

count = {}
for i in items:
    count[i] = count.get(i, 0) + 1

print("Purchase frequency:")
for k in count:
    print(k, count[k])

mx = max(count, key=count.get)
print("\nMost popular item:", mx)

print("\nPurchased once:", end=" ")
for k in count:
    if count[k] == 1:
        print(k, end=" ")

print("\n\nSorted by frequency:")
for k in sorted(count, key=count.get, reverse=True):
    print(k, count[k])
