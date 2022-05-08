n = int(input())
input()

for i in range(n):
    a = int(input())
    b = int(input())

    for m in range(b):
        for n in range(a):
            print(str(n+1) * (n+1))

        for n in range(a-1, 0, -1):
            print(str(n) * n)

        print()