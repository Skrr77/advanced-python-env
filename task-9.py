ticket = input("Enter a 6-digit ticket number: ")


sum_first = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
sum_last = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

print("YES" if sum_first == sum_last else "NO")