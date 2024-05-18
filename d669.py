while True:
    try:
        a, b, c, d = map(int, input().split())
        if a == b == c == d == 0:
            break

        t1 = a * 60 + b
        t2 = c * 60 + d
        if t1 > t2:
            t2 += 24 * 60
        print(abs(t1 - t2))
    except:
        break