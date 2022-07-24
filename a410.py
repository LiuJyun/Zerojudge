a, b, c, d, e, f = map(int, input().split())
delta = a * e - d * b
x = c * e - f * b
y = a * f - d * c
if delta != 0:
    print('x={:.2f}'.format(x / delta))
    print('y={:.2f}'.format(y / delta))
else:
    if x == 0 and y == 0:
        print('Too many')
    else:
        print('No answer')