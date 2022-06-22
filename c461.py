a, b, c = map(int, input().split())

a = 0 if a == 0 else 1
b = 0 if b == 0 else 1

temp = False
if (a and b) == c:
    print('AND')
    temp = True
if (a or b) == c:
    print('OR')
    temp = True
if (a ^ b) == c:
    print('XOR')
    temp = True

if not temp:
    print('IMPOSSIBLE')