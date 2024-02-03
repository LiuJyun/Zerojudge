while True:
    try:
        a, b = map(int, input().split())
        if a % b == 0 or a == 0:
            print('Ok!')
        else:
            print('Impossib1e!')
    except:
        break