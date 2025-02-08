a = int(input())
b = [int(x) for x in input().split()]
for j in range(len(b)):
    if b[j] % 3 == 0 and b[j] % 2 == 0:
        print(1, end=' ')
    elif b[j] % 2 != 0 and b[j] % 3 != 0:
        print(2, end=' ')
    elif ((b[j] ** 0.5) % 1 == 0)or (b[j] % 7 != 0 and b[j] % 2 == 0):
        print(3, end=' ')
    else:
        print(0, end=' ')