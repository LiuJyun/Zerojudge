while True:
    try:
        input()
        n = input().split()
        a = [[], [], [], [], [], [], [], [], [], []]
        for i in n:
            a[int(i)%10].append([int(i)//10, i])
        for j in a:
            j.sort(reverse=True)
            for k in j:
                print(k[-1], end=' ')
        print()
    except:
        break