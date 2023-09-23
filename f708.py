m, n = map(int, input().split())
a = [int(x) for x in input().split()]
g = [int(x) for x in input().split()]

if m > n:
    ha = sum(a)
    hg = sum(g)

    if ha > hg:
        print('Yes')
    else:
        print('No')
else:
    print('No')