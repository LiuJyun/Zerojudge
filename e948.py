n = int(input())
l = []
for i in range(n):
    g, a, h, w = map(int, input().split())
    if g == 1:
        b = (13.7 * w) + (5.0 * h) - (6.8 * a) + 66
    else:
        b = (9.6 * w) + (1.8 * h) - (4.7 * a) + 655
    l.append(b)

for i in l:
    print('{:.2f}'.format(i))
