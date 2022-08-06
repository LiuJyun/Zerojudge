n = int(input())
a = [int(x) for x in input().split()]
b = []
c = []

for i in range(n):
    if a[i] % 2 == 0:
        b.append(a[i])
    else:
        c.append(a[i])

bb = sorted(b)
cc = sorted(c, reverse = True)

bb = [str(x) for x in bb]
cc = [str(x) for x in cc]
print(' '.join(bb), end=' ')
print(' '.join(cc))