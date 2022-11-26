n, d = map(int, input().split())
a = [int(x) for x in input().split()]

t = 0
c = a[0]
for i in range(1, len(a)):
    if c == 0:
        c = a[i]
    elif a[i] > c + d:
        t += a[i] - c
        c = 0
print(t)