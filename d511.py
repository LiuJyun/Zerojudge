s = 0
for i in range(5):
    a = [int(i) for i in input().split()]
    a.sort()
    if a[0] + a[1] > a[2]:
       s = s + 1
print(s)