while True:
    try:
        a, b = map(int, input().split())
        print(a+int(a/b)+int((int(a/b)+a%b)/b))
    except:
        break