while True:
    try:
        b = int(input())
        break
    except:
        continue

for k in range(b):
    a = []
    n = int(input())
    for i in range(n):
        a.append(input().split())
    m = int(input())
    for i in range(m):
        p = int(input())
        c = 0
        t = True
        d = ''
        for j in range(n):
            if p >= int(a[j][1]) and p < int(a[j][2]):
                d = a[j][0]
                c += 1
                t = False
        if t or c > 1:
            print('UNDETERMINED')
        elif c == 1:
            print(d)