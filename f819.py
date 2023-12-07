n = int(input())

id = []
cost = 0
for i in range(n):
    a, b = map(int, input().split())

    if b > 100:
        cost += (b - 100) * 5
        id.append(a)

if len(id) == 0:
    print(0)
else:
    print(' '.join(str(s) for s in sorted(id)))
    print(cost)