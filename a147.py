while True:
    try:
        n = int(input())
        t = []
        for i in range(n):
            if i % 7 != 0:
                t.append(str(i))
        print(' '.join(t))
    except:
        break