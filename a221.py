while True:
    try:
        n = int(input())
        for i in range(n):
            a = input()
            b = input()

            if a == b:
                print('Case {}: Yes'.format(i+1))
            else:
                c = a.replace(' ', '')
                d = b.replace(' ', '')

                if c == d:
                    print('Case {}: Output Format Error'.format(i+1))
                else:
                    print('Case {}: Wrong Answer'.format(i+1))

    except:
        break
