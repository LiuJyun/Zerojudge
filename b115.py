while True:
    try:
        a = int(input())
        b = input()
        c = int(input())
        if b == '*':
            print(a * b)
        else:
            print(a // b)
    except:
        break