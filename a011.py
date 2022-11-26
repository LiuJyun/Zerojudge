while True:
    try:
        s = input()
        l = []
        ss = ''
        for i in s:
            if i.isalpha() or i.isspace():
                ss += i
            else:
                ss += ' '
        print(len(ss.split()))
    except:
        break