n = int(input())
a = []
fail = 0
for i in range(n):
    a.append(input())

for i in range(10):
    s = input()
    if s[0] != 'B' or not s[1:3].isdigit() or s[3:7] not in a or s[-2] < '0' or s[-2] > '9' or s[-1] < '0' or s[-1] > '9':
        fail += 1
        print('N')
        continue
    print('Y')

if fail/10 == 0.0:
    print(0)
else:
    print('{:.1f}'.format(fail/10))