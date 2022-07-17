import datetime
n = int(input())

for i in range(n):
    input()
    s1 = [int(x) for x in input().split('/')]
    s2 = [int(x) for x in input().split('/')]
    d1 = datetime.datetime(s1[2], s1[1], s1[0])
    d2 = datetime.datetime(s2[2], s2[1], s2[0])
    interval = (d1 - d2)

    print(interval.days)