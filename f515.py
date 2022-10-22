a = input().split()
for i in a:
    if i.lower() == 'for':
        print('4', end='')
    elif i.lower() == 'to':
        print('2', end='')
    elif i.lower() == 'and':
        print('n', end='')
    elif i.lower() == 'you':
        print('u', end='')
    else:
        print(i[0].upper(), end='')