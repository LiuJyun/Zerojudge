while True:
    try:
        a, b = map(int, input().split())
        print(int((a+b)*2))
    except:
        break