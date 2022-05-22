d = {}
n = int(input())
for i in range(n):
    s = int(input()[-3:])
    if int(s/10) in d:
        d[int(s/10)] = d[int(s/10)] + 1
    else:
        d[int(s / 10)] = 1

for i in sorted(d):
    print(i, d[i])