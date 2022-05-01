while True:
    try:
        input()
        print(' '.join([str(x) for x in sorted([int(x) for x in input().strip().split()])]))
    except:
        break