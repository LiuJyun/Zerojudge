n = int(input())
for i in range(n):
    s = input()
    a = ''
    c = ''
    print('Case {}: '.format(i+1), end='')
    for i in range(len(s)):
        if s[i].isalpha():
            if i != 0:
                print(a * int(c), end='')
                c = ''
                a = ''
            a = s[i]
        else:
            c += s[i]
    print(a * int(c))