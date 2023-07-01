n = int(input())
l = []
for i in range(n):
    l.append(input().split())
s = input()

r = []
for i in range(len(l)):
    if s == l[i][1]:
        r.append(l[i][0])

if len(r) == 0:
    print('No')
else:
    rr = sorted(r)
    for i in rr:
        print(i)
