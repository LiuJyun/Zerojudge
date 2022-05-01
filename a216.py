while True:
    try:
        n = int(input())
        print('{} {}'.format((n*(n+1))//2, (n*(n+1)*(n+2))//6))
    except:
        break