dic = {10: 'A', 9: 'A', 8: 'B', 7: 'C', 6: 'D'}
n = int(input())
for i in range(n):
    a = [int(x) for x in input().split()]
    c = [a[-1], a[-2], a[-3]]
    c.sort()

    total = (sum(a[:4]) + (c[-1] + c[-2]) // 2) // 10
    if total >= 6 and total <= 10:
        print('Case {}: {}'.format(i + 1, dic[total]))
    else:
        print('Case {}: {}'.format(i + 1, 'F'))