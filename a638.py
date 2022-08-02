import math

n = int(input())
a = []
b = []

for i in range(n):
    a.append([int(x) for x in input().split()])

for i in range(n):
    for j in range(i+1, n):
        b.append(math.sqrt((a[i][0] - a[j][0]) ** 2 + (a[i][1] - a[j][1]) ** 2))

print('{:.4f}'.format(min(b)))