while True:
    try:
        n = input()
        for i in range(1, len(n)):
            print(abs(ord(n[i]) - ord(n[i-1])), end='')
        print()
    except:
        break