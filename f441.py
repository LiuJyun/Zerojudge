n, s = map(int, input().split())
a = input().split()
m = int(input())
for i in range(m):
    x = input().split()
    sum = 0
    for j in range(n):
        if a[j] == x[j]:
            sum += s
    print(sum)