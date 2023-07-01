n = int(input())
l = []
for i in range(n):
    l.append([int(x) for x in input().split()])
ll = sorted(l, key=lambda l: (l[0], l[1]))

for i in range(n):
    print(ll[i][0], ll[i][1])
