while True:
    try:
        n = int(input())
        for i in range(n):
            a = input().split()
            if a[0] == '1':
                print(int(a[1]) + int(a[2]))
            elif a[0] == '2':
                print(int(a[1]) - int(a[2]))
            elif a[0] == '3':
                print(int(a[1]) * int(a[2]))
            elif a[0] == '4':
                print(int(a[1]) // int(a[2]))
    except:
        break
