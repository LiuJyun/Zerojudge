n = int(input())
a = [int(x) for x in input()]
l = []
for i in range(-1, -1*len(a) - 1, -1*n):
    if i + 1 == 0:
        l.append(sum(a[i - n + 1: len(a)]))
    elif i - n + 1 == -1*len(a):
        l.append(sum(a[-1*len(a): i + 1]))
    else:
        l.append(sum(a[i - n + 1: i + 1]))

if len(set(l)) == len(l):
    print('No')
else:
    print('Yes')
