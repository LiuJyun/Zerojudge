n = int(input())
for i in range(n):
    m = int(input())
    a = [int(x) for x in input().split()]
    c = 0
    for i in range(m):
        for j in range(0, m- i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                c += 1
    print('Optimal train swapping takes {} swaps.'.format(c))