import math

while 1:
    try:
        n = int(input())

        for i in range(n):
            a = [int(x) for x in input().split()]
            d = a[1] * a[1] - 4 * a[0] * a[2]
            if d < 0 or math.sqrt(d) * math.sqrt(d) != d:
                print('No')
            else:
                print('Yes')
    except:
        break