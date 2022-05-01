while True:
    try:
        n = input().split()
        for i in range(len(n)):
            n[i] = int(n[i])
        if sum(n[1:]) / (len(n) - 1) > 59:
            print('no')
        else:
            print('yes')
    except:
        break