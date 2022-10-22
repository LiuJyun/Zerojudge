n = int(input())
a = [int(x) for x in input().split()]
for i in range(n, 0, -1):
    if i not in a:
        print('No. {}'.format(i))