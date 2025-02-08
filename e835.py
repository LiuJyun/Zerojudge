a = int(input())
c = []
if 0 < a <= 2500:
    if a % 25 != 0:
        d = (a // 25) + 1
    else:
        d = a // 25
    if a % 25 == 0:
        e = 25
    else:
        e = a % 25
    c.append(1)
    c.append(d)
    c.append(e)
elif 2500 < a <= 7500:
    if a % 50 != 0:
        d = ((a - 2500) // 50) + 1
    else:
        d = (a - 2500) // 50
    if a % 50 == 0:
        e = 50
    else:
        e = a % 50
    c.append(2)
    c.append(d)
    c.append(e)
elif a > 7500:
    if a % 25 != 0:
        d = ((a - 7500) // 25) + 1
    else:
        d = (a - 7500) // 25
    if a % 25 == 0:
        e = 25
    else:
        e = a % 25
    c.append(3)
    c.append(d)
    c.append(e)
for i in range(len(c)):
    print(c[i], end=' ')