while True:
    try:
        a, b = map(int, input().split())

        t = True
        for i in range(a, b, 1):
            s = str(i)
            sum = 0
            for j in s:
                sum += int(j) ** len(s)
            if sum == i:
                print(sum, end=' ')
                t = False
        if t:
            print('none')
    except:
        break