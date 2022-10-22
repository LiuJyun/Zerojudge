a = [int(x) for x in input().split()]
print(a.count(max(a, key=a.count)), end=' ')
b = sorted(set(a), reverse=True)
for i in b:
    print(i, end=' ')