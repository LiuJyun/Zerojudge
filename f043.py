r, a = map(int, input().split())
if r == a:
    a -= 3
b = r - a
print('{}+{}={}'.format(min([a, b]), max([a, b]), r))