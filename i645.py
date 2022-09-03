from itertools import combinations
a = 'abcdefghijklmnopqrstuvwxyz'

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    l = list(combinations(a[:n], m))
    for i in l:
        for j in i:
            print(j, end='')
        print()
