n, m = map(int, input().split())
for i in range(n):
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))

    c = a.intersection(b)
    print(len(c))
