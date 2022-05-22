while True:
    try:
        a = float(input())
        print('|{:0.4f}|={:0.4f}'.format(a, abs(a)))
    except:
        break