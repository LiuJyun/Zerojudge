from itertools import permutations
a = 'abcdefghijklmnopqrstuvwxyz'

while True:
    n = int(input())
    if n == 0:
        break

    l = list(permutations(a[:n], n))
    for i in l:
        for j in i:
            print(j, end='')
        print()
