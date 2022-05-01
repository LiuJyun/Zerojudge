while True:
    try:
        a, b = map(int, input().split())
        sum = 0
        for i in range(a, b + 1):
            temp = True
            for j in range(2, i):
                if i % j == 0:
                    temp = False
                    break
            if temp:
                sum += 1
        print(sum)
    except:
        break