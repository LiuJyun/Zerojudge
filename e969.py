d = {0: ['eats an Apple pie', 32], 1: ['drinks a Corn soup', 55]}
t = 0
temp = 0

n, m, k = map(int, input().split())
while True:
    if n < d[k][1]:
        break

    n -= d[k][1]
    if n == 0:
        print('{}: Wayne {}, and now he doesn\'t have money.'.format(t, d[k][0]))
    elif n == 1:
        print('{}: Wayne {}, and now he has {} dollar.'.format(t, d[k][0], n))
    else:
        print('{}: Wayne {}, and now he has {} dollars.'.format(t, d[k][0], n))
    t += m
    k = (k + 1) % 2
    temp = 1

if not temp:
    print('Wayne can\'t eat and drink.')