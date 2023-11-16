a, b = map(int, input().split())
if b == 0:
    print('OK!')
else:
    if a % b == 0:
        print('OK!')
    else:
        c = a // b
        print(a - c * b)