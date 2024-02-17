d = {}
s = input()
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
dd = sorted(d.items(), key=lambda x: (-x[1], x[0]))
for i in dd:
    print(i[0], end='')