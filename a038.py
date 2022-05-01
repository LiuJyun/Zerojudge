while True:
    try:
        s = input()
        temp = True
        for i in range(len(s)-1, -1, -1):
            if s[i] != '0' or temp == False:
                print(s[i], end='')
                temp = False
        if temp:
            print('0')
        print()
    except:
        break