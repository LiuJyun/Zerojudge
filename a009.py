while True:
    try:
        s = input()
        for i in s:
            print(chr(ord(i) - 7), end="")
        print()

    except:
        break