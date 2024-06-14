n = int(input())
a = [int(x) for x in input().split()]

total = (a[0] - 1) * 3
for i in range(1, n):
    if a[i] - a[i - 1] > 0:
        total += (a[i] - a[i - 1]) * 3
    else:
        total += (a[i - 1] - a[i]) * 2

print(total)