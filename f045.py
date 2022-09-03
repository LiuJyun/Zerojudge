s = [int(x) for x in input()]
ss = sorted(s)
if s[-1] + s[-2] * 10 + s[-3] * 100 == ss[-1] ** 2 + ss[-2] ** 2:
    print('Good Morning!')
else:
    print('SPY!')