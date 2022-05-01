while True:
    try:
        n, m = map(int, input().split())
        if m == -1:
            print(1)
        else:
            count = 0
            sum = 0
            while True:
                sum += n
                n += 1
                count += 1

                if sum > m:
                    break
            print(count)
    except:
        break