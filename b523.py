l = []
while True:
    try:
        s = input()
        if s in l:
            print('YES')
        else:
            print('NO')
            l.append(s)
    except:
        break