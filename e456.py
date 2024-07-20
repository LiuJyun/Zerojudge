a = input().split()
for i in range(len(a) - 1):
    print('{} little, '.format(a[i]), end='')
print('{} little Indians'.format(a[-1]))