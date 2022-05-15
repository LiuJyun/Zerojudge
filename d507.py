a = [int(i) for i in input().split()]
a.sort()
if a[0] ** 2 + a[1] ** 2 < a[2] ** 2:
    print('obtuse triangle')
elif a[0] ** 2 + a[1] ** 2 == a[2] ** 2:
    print('right triangle')
else:
    print('acute triangle')