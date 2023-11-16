while True:
    try:
        n = input()
        t = 1
        for i in range(1, len(n)):
            if n[i] != n[i-1]:
                if t == 1:
                    print(n[i - 1], end='')
                elif t == 2:
                    print(n[i - 1]*2, end='')
                else:
                    print(t, n[i-1], sep='', end='')
                t = 1
            else:
                t += 1

        if t == 1:
            print(n[-1])
        elif t == 2:
            print(n[-1] * 2)
        else:
            print(t, n[-1], sep='')

    except:
        break