n = int(input())
l = [int(x) for x in input().split()]
m = [int(x) for x in input().split()]
ll = []
mm = []
for i in range(n):
    if l[i] > m[i]:
        ll.append(i+1)
    else:
        mm.append(i+1)

if len(ll) != 0:
    print(' '.join(map(str, ll)))
else:
    print(-1)

if len(mm) != 0:
    print(' '.join(map(str, mm)))
else:
    print(-1)