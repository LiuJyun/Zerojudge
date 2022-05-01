while True:
    try:
        n = int(input())
        sum = 0
        if n <= 10:
            sum += n * 6
        elif n <= 20:
            sum += (n - 10) * 2 + 60
        elif n <= 40:
            sum += (n - 20) + 80
        else:
            sum = 100
        print(sum)
    except:
        break