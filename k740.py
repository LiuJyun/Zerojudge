a = [[1], [1, 1]]
n = int(input())
for i in range(2, n):
    l = []
    for j in range(i + 1):
        if j == 0 or j == i:
            l.append(1)
        else:
            # l.append(0)
            l.append(a[i - 1][j - 1] + a[i - 1][j])
    a.append(l)

for i in range(n):
    for j in range(i + 1):
        print(a[i][j], end=' ')
    print()
