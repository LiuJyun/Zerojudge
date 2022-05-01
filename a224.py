while True:
    try:
        c = [0] * 26
        n = input().lower()
        for i in n:
            if 'a' <= i <= 'z':
                c[ord(i) - 97] += 1

        temp = 0
        for i in c:
            if i % 2 == 1:
                temp += 1

        if temp <= 1:
            print('yes !')
        else:
            print('no...')
    except:
        break