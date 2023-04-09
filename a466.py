a = ['one', 'two', 'three']
n = int(input())
for n in range(n):
    s = input()

    if len(s) == 5:
        print(3)
    else:
        c1 = 0
        c2 = 0
        for i in range(3):
            if s[i] == a[0][i]:
                c1 += 1
            elif s[i] == a[1][i]:
                c2 += 1

        if c1 >= 2:
            print(1)
        elif c2 >= 2:
            print(2)