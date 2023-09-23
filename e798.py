n = int(input())
l = []
for i in range(n):
    l.append([int(x) for x in input().split()])

ll = []
for i in range(0, n, 2):
    t = []
    for j in range(0, n, 2):
        t.append(max(l[i][j], l[i][j+1], l[i+1][j], l[i+1][j+1]))
    ll.append(t)

for i in range(len(ll)):
    for j in range(len(ll[i])):
        print(ll[i][j], end=' ')
    print()