while True:
    try:
        n = int(input())
        for i in range(n):
            m = input()
            sum = 1
            for j in m:
                sum *= int(j)
            print(sum)
    except:
        break