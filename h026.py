f = int(input())
n = int(input())
y = [int(x) for x in input().split()]
ff = []
t = False
i = 0

for i in range(n):
    # print(i, y[i], f)

    if f == 0 and y[i] == 2 or f == 2 and y[i] == 5 or f == 5 and y[i] == 0:
        ff.append(f)
        for j in ff:
            print(j, end=' ')
        print(': Won at round {}'.format(i + 1))
        t = True
        break
    elif y[i] == 0 and f == 2 or y[i] == 2 and f == 5 or y[i] == 5 and f == 0:
        ff.append(f)
        for j in ff:
            print(j, end=' ')
        print(': Lost at round {}'.format(i + 1))
        t = True
        break
    else:
        ff.append(f)
        if i >= 1 and y[i] == y[i-1]:
            if y[i] == 2:
                f = 0
            elif y[i] == 5:
                f = 2
            elif y[i] == 0:
                f = 5
        else:
            f = y[i]

if not t:
    for j in ff:
        print(j, end=' ')
    print(': Drew at round {}'.format(i + 1))