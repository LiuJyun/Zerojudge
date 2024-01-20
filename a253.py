d = {}
while True:
    a = [int(x) for x in input().split()]
    if a[0] == -1:
        break
    if a[0] not in d:
        d[a[0]] = a[1]

while True:
    a = [int(x) for x in input().split()]
    if a[0] == -1:
        break
    if a[0] not in d:
        d[a[0]] = a[1]
    else:
        d[a[0]] += a[1]

for k, v in sorted(d.items()):
    print(k, v)
