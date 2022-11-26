m, a = map(int, input().split())
t = [int(x) for x in input().split()]
for i in range(m):
    if t[i] < a:
        a += t[i]
    else:
        break
print(a)