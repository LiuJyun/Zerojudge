n = int(input())
a = input().split()
if n % 2 == 0:
    print((int(a[n//2 - 1]) + int(a[n//2])) // 2)
else:
    print(a[n // 2])