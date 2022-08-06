while True:
    try:
        a = input().split()
        if a[0] == 'END':
            break
        s = ''
        for i in a:
            s += i[0].upper()
        print('{} {}'.format(s, a[-1]))
    except:
        break