n = int(input())
for i in range(n):
    a = [int(x) for x in input().split()]
    if a[2] * 60 + a[3] - a[0] * 60 - a[1] >= a[4]:
        print('Yes')
    else:
        print('No')