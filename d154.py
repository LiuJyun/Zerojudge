# import math
#
# n = int(input())
# for i in range(n):
#     a = input().split()
#     g = math.gcd(int(a[0]), int(a[2]))
#     print(int(a[0])//g, a[1], int(a[2])//g)

import math
n = int(input(''))
for i in range(0, n):
    p, b, q = input('').split()
    p = int(p)
    q = int(q)
    a = math.gcd(p, q)
    print('{} / {}'.format(p//a, q//a))