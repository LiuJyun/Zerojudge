s = input()
a = input()

b = []
for i in s:
    for j in a:
        if i == j:
            b.append(j)
n = int(input())
for k in range(n):
    t = int(input())
    print(b[t])