import math

n = int(input())
for i in range(n):
    a = input().split()
    g = math.gcd(int(a[0]), int(a[2]))
    print(int(a[0])//g, a[1], int(a[2])//g)