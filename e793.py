def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(gcd(a, b))