while True:
    try:
        v, r = map(float, input().split())
        print('{:.4f}'.format(1000 * v/r))
    except:
        break