dic = {}
s = input()
for i in s:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

d = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
for i in range(len(d)):
    print(d[i][0], end = ' ')