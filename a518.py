while True:
    try:
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break

        if a > b:
            a, b = b, a
        m = min([b-a, a+100-b])
        print(m)

    except:
        break