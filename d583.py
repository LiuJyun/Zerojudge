while True:
    try:
        n = int(input())
        a = [int(x) for x in input().split()]
        for i in sorted(a):
            print(i, end=' ')
        print()
    except:
        break