n = int(input())
l = []
f = 0
for i in range(n):
    l.append([int(x) for x in input().split()])
    if l[i][1] == -1:
        f += 1
ll = sorted(l, key=lambda row: (row[1]), reverse=True)
s = ll[0][1] - n - f * 2
if s < 0:
    s = 0
print(s, ll[0][0])
