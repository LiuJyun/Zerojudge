n = int(input())
for i in range(n):
    a, b, c = map(int, input().split())
    temp = False
    for j in range(a+1, b, 1):
        if j % c != 0:
            print(j, end=' ')
            temp = True
    print()
    if not temp:
        print('No free parking spaces.')