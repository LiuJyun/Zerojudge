while True:
    try:
        a = input()
        b = input()
        print((ord(b[0]) - ord(a[0])) % 26)
    except:
        break