n = int(input())

for i in range(n):
    a = int(input())
    b = int(input())

    sum = 0
    for j in range(a, b + 1, 1):
        if j % 2 == 1:
            sum = sum + j
    print('Case {}: {}'.format((i + 1), sum))