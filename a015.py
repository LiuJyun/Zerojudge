while True:
    try:
        m, n = map(int, input().split())
        num = []
        for i in range(m):
            num.append(input().split())

        for i in range(n):
            for j in range(m):
                if j != m-1:
                    print(num[j][i], end=' ')
                else:
                    print(num[j][i])
    except:
        break