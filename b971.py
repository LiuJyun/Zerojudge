a, b, c = map(int, input().split())
n = abs((b - a) // c) + 1
for i in range(n):
    print(a, end=' ')
    a = a + c