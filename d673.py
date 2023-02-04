c = 1
while True:
    try:
        n = int(input())
        if n == -1:
            break

        a = [int(x) for x in input().split()]
        b = [int(x) for x in input().split()]
        t = n

        print('Case {}:'.format(c))
        for i in range(len(b)):
            if t >= b[i]:
                print('No problem! :D')
                t -= b[i]
            else:
                print('No problem. :(')

            t += a[i]
        c += 1
    except:
        break