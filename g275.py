n = int(input())
for j in range(n):
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    temp = 1
    # A: 二四不同二六同：每一句第二、四個字必須不同平仄，而第二、六個字必須相同平仄
    if a[1] == a[3] or b[1] == b[3] or a[1] != a[5] or b[1] != b[5]:
        print('A', end='')
        temp = 0

    # B: 仄起平收：第一句的結尾必須為仄聲，第二句的結尾必須為平聲
    if a[-1] != 1 or b[-1] != 0:
        print('B', end='')
        temp = 0

    # C: 上下相對：第一、二句的第二、四、六個字平仄必須不同
    if a[1] == b[1] or a[3] == b[3] or a[5] == b[5]:
        print('C', end='')
        temp = 0

    if temp:
        print('None', end='')
    print()