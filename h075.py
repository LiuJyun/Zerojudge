n = int(input())
l = []
for i in range(n):
    t = [int(x) for x in input().split()]
    avg = (t[1] * 5 + t[2] * 3 + t[3] * 2) / 10
    if avg == int(avg):
        avg = int(avg)
    l.append([t[0], t[1], t[2], t[3], avg])

ll = sorted(l, key=lambda row: (row[4], row[1], row[2], row[3]), reverse=True)
for i in range(len(ll)):
    print(ll[i][0], ll[i][4])