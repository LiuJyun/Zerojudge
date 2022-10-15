n = int(input())
a = [0, 0, 0]
t = 0
for i in range(n):
    s = input().strip()

    if s == 'Get_Kill':
        a[0] += 1
        t += 1
        if t < 3:
            print('You have slain an enemie.')
        elif t == 3:
            print('KILLING SPREE!')
        elif t == 4:
            print('RAMPAGE~')
        elif t == 5:
            print('UNSTOPPABLE!')
        elif t == 6:
            print('DOMINATING!')
        elif t == 7:
            print('GUALIKE!')
        else:
            print('LEGENDARY!')

    elif s == 'Get_Assist':
        a[2] += 1

    elif s == 'Die':
        if t < 3:
            print('You have been slained.')
        else:
            print('SHUTDOWN.')
        t = 0
        a[1] += 1
    # print(s, a)
print('{}/{}/{}'.format(a[0], a[1], a[2]))