a = []
while True:
    try:
        a.append(int(input()))
        a.sort()
        if len(a) % 2 == 0:
            print((a[len(a) // 2] + a[len(a) // 2 - 1]) // 2)
        else:
            print(a[len(a) // 2])
    except:
        break