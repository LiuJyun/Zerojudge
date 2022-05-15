input()
a = [int(i) for i in input().split()]
s = 0
for i in range(len(a)):
    if a[i] <= 10:
        s = s + 1
print(s)