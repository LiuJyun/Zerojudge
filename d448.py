while True:
    try:
        t1, t2, t3, x1, x3 = map(float, input().split())
        x2 = x1 - (t1 - t2) * (x1 - x3) / (t1 - t3)
        print('{:.6f}'.format(x2))
    except:
        break