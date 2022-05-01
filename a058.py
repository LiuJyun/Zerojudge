while True:
    try:
        n = int(input())
        num = [0, 0, 0]
        for i in range(n):
            num[int(input())%3] += 1
        print('{} {} {}'.format(num[0], num[1], num[2]))
    except:
        break