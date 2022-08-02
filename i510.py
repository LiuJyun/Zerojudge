while True:
    try:
        a, b = map(int, input().split())
        c, d = input().split()
        if d in c:
            print('Yes')
            print('pos: {}'.format(c.find(d)))
        else:
            print('No')
    except:
        break