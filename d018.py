while True:
    try:
        a = input().split()

        summ = 0
        for i in a:
            b = i.split(':')
            if int(b[0]) % 2 == 0:
                summ -= eval(b[1])
            else:
                summ += eval(b[1])

        print('{:g}'.format(summ))

    except:
        break