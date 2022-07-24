a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

t1 = a[0] * 60 + a[1]
t2 = b[0] * 60 + b[1]

if t1 > t2:
    t2 = (b[0]+24) * 60 + b[1]

print((t2-t1) // 60, (t2-t1) % 60)