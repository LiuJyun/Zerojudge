dic = {'T': 1.0, 'U': 30.9, 'J': 0.28, 'E': 34.5}

S = input()
if "\r" in S:
    a = float(S.split("\r")[0])
    b = S.split("\r")[1].split()
else:
    a = float(S)
    b = input().split()

c = a / dic[b[1]] - int(b[0])
if c >= 0.05:
    print('{} {:0.2f}'.format(b[1], c))
elif c >= 0:
    print('{} {:0.2f}'.format(b[1], 0))
else:
    print('No Money')