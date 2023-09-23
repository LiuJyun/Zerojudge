while True:
    n = input()
    if n == '0':
        break

    while True:
        # print(n)
        s = 0
        for i in n:
            s += int(i)
        n = str(s)
        if len(n) <= 1:
            break
    print(s)