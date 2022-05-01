import datetime

while True:
    try:
        n = input().split()
        d1 = datetime.datetime(int(n[0]), int(n[1]), int(n[2]))
        n = input().split()
        d2 = datetime.datetime(int(n[0]), int(n[1]), int(n[2]))
        print(abs((d1 - d2).days))
    except:
        break