while True:
    try:
        n = int(input())
        print('{}! = '.format(n), end='')
        sum = 1
        if n == 0:
            print('1 ', end='')
        else:
            for i in range(n, 0, -1):
                print('{} '.format(i), end='')
                sum *= i

                if i != 1:
                    print('* ', end='')
        print('= {}'.format(sum))
    except:
        break