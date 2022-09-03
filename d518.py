from sys import stdin

for s in stdin:
    l = {}
    n = int(s)
    a = 1
    for i in range(n):
        s = stdin.readline().strip()
        if s in l:
            print('Old! {}'.format(l[s]))
        else:
            l[s] = a
            a += 1
            print('New! {}'.format(l[s]))