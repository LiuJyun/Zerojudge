from sys import stdin

f = [1]
t = 2
for i in range(10000):
    f.append(t)
    t *= 2

for s in stdin:
    n = int(s)
    if (n == 0): break
    print(f[n])