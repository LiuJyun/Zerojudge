input()
a = [int(x) for x in input().split()]
d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 0

dd = dict(sorted(d.items(), key=lambda item: -item[1]))
print(len(dd))
count = 0
temp = []
for k, v in dd.items():
    temp.append([k, v])

if len(temp) == 1:
    print(temp[0][0])
else:
    if temp[0][1] == temp[len(temp) - 1][1]:
        print('NO')
    else:
        for i in range(0, len(temp) - 1, 1):
            print(temp[i][0], end=' ')
            if temp[i][1] != temp[i + 1][1]:
                break