import math

n, t = map(int, input().split())
n2 = n // math.gcd(n, t)
t2 = t // math.gcd(n, t)

print(int(math.log2(n2+t2)))