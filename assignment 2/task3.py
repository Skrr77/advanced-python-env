s = input()

a, op, b, _, c = s

if a == 'x':
    print(int(c) - int(b) if op == '+' else int(c) + int(b))
elif b == 'x':
    print(int(c) - int(a) if op == '+' else int(a) - int(c))
else:
    print(int(a) + int(b) if op == '+' else int(a) - int(b))