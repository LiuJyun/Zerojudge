while True:
    try:
        n, m = map(int, input().split())
        if n > m:
            print(m+1)
        elif n == m:
            print(m)
    except:
        break