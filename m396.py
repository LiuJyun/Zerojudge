a = [int(x) for x in input().split()]
if a[0] >= sum(a[1:]):
    print(sum(a[1:]))
else:
    print(-1)