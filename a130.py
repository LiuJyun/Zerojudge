n = int(input())
for i in range(n):
    l = []
    for j in range(10):
        l.append(input().split())
        l[j][1] = int(l[j][1])
    l.sort(key=lambda row: -row[1])

    print('Case #{}:'.format(i + 1))
    for j in range(10):
        if l[j][1] == l[0][1]:
            print(l[j][0])
        else:
            break