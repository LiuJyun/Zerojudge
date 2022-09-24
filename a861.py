while True:
    try:
        a, b = map(int, input().split())
        print(2 * a + 2 * b)
    except:
        break